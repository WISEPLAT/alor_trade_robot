import backtrader as bt


class PrintStatusAndBars(bt.Strategy):
    """
    - Отображает статус подключения
    - При приходе нового бара отображает его цены/объем
    - Отображает статус перехода к новым барам
    """
    params = (  # Параметры торговой системы
        ('name', None),  # Название торговой системы
        ('symbols', None),  # Список торгуемых тикеров. По умолчанию торгуем все тикеры
    )

    def log(self, txt, dt=None):
        """Вывод строки с датой на консоль"""
        dt = bt.num2date(self.datas[0].datetime[0]) if not dt else dt  # Заданная дата или дата последнего бара первого тикера ТС
        print(f'{dt.strftime("%d.%m.%Y %H:%M")}, {txt}')  # Выводим дату и время с заданным текстом на консоль

    def __init__(self):
        """Инициализация торговой системы"""
        self.isLive = False  # Сначала будут приходить исторические данные
        self.order = None
        self.orders_bar_executed = {}

    def start(self):
        for data in self.datas:  # Пробегаемся по всем запрошенным тикерам
            ticker = data._dataname  # имя тикера
            self.orders_bar_executed[ticker] = 0

    def next(self):
        """Приход нового бара тикера"""
        # if self.p.name:  # Если указали название торговой системы, то будем ждать прихода всех баров
        #     lastdatetimes = [bt.num2date(data.datetime[0]) for data in self.datas]  # Дата и время последнего бара каждого тикера
        #     if lastdatetimes.count(lastdatetimes[0]) != len(lastdatetimes):  # Если дата и время последних баров не идентичны
        #         return  # то еще не пришли все новые бары. Ждем дальше, выходим
        #     print(self.p.name)
        for data in self.datas:  # Пробегаемся по всем запрошенным тикерам
            if not self.p.symbols or data._name in self.p.symbols:  # Если торгуем все тикеры или данный тикер
                self.log(f'{data._name} - {bt.TimeFrame.Names[data.p.timeframe]} {data.p.compression} - Open={data.open[0]:.2f}, High={data.high[0]:.2f}, Low={data.low[0]:.2f}, Close={data.close[0]:.2f}, Volume={data.volume[0]:.0f}',
                         bt.num2date(data.datetime[0]))

                ticker = data._dataname  # имя тикера
                _close = data.close[0]  # текущий close
                _low = data.low[0]  # текущий low
                _high = data.high[0]  # текущий high
                _open = data.open[0]  # текущий close

                # Проверка, мы в рынке?
                if not self.position:
                    # Ещё нет... мы МОГЛИ БЫ КУПИТЬ, если бы...
                    if self.data.close[0] < self.data.close[-1]:
                        # текущее закрытие меньше предыдущего закрытия
                        if self.data.close[-1] < self.data.close[-2]:
                            # ПОКУПАЙ, ПОКУПАЙ, ПОКУПАЙ!!! (с параметрами по умолчанию)
                            self.log('BUY CREATE, %.2f' % self.data.close[0])
                            # Следим за созданным ордером, чтобы избежать второго дублирующегося ордера
                            self.order = self.buy(data=data)  # , size=size)
                else:
                    # Уже в рынке? ... мы могли бы продать
                    try:
                        # продаём после 5 баров от момента покупки...
                        if len(self) >= (self.orders_bar_executed[data._name] + 5):
                            # ПРОДАВАЙ, ПРОДАВАЙ, ПРОДАВАЙ!!! (с параметрами по умолчанию)
                            self.log('SELL CREATE, %.2f' % self.data.close[0])
                            # Следим за созданным ордером, чтобы избежать второго дублирующегося ордера
                            self.order = self.sell(data=data)
                    except:
                        print("error...")

    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log('OPERATION PROFIT, GROSS %.2f, NET %.2f' % (trade.pnl, trade.pnlcomm))

    def notify_order(self, order):
        ticker = order.data._name
        size = order.size

        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Проверка, мы в рынке?
        # Внимание: брокер может отклонить заявку, если недостаточно денег
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

            self.bar_executed = len(self)
            self.orders_bar_executed[order.data._name] = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Запись: отложенного ордера - нет
        self.order = None

    def notify_data(self, data, status, *args, **kwargs):
        """Изменение статуса приходящих баров"""
        data_status = data._getstatusname(status)  # Получаем статус (только при LiveBars=True)
        print(f'{data._name} - {self.p.name} - {data_status}')  # Статус приходит для каждого тикера отдельно
        self.isLive = data_status == 'LIVE'  # В Live режим переходим после перехода первого тикера
