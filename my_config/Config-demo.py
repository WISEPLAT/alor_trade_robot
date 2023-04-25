# Чтобы получить Refresh Token:
# 0. Для получения тестового логина/пароля демо счета оставить заявку в Telegram на https://t.me/AlorOpenAPI
# 1. Зарегистрироваться на https://alor.dev/login
# 2. Выбрать "Токены для доступа к API"

# Для реального счета:
# 1. Привязать торговый аккаунт
# 2. Выписать токен

# Для демо счета:
# 1. Пройти по ссылке "Токены для ведения торгов в тестовом контуре" - "Begin OAuth authorization flow"
# 2. Ввести тестовый логин/пароль. Нажать "Разрешить"

# Как заполнять переменные портфелей PortfolioStocks, PortfolioFutures, PortfolioFx:
# 1. Запустить скрипт "Examples/02 - Accounts.py"
# 2. Получить портфели для всех рынков
# 3. Заполнить переменные полученными значениями

# Коды торговых серверов для стоп заявок:
TradeServerCode = 'TRADE'  # Рынок Ценных Бумаг
ITradeServerCode = 'ITRADE'  # Рынок Иностранных Ценных Бумаг
FutServerCode = 'FUT1'  # Фьючерсы
OptServerCode = 'OPT1'  # Опционы
FxServerCode = 'FX1'  # Валютный рынок


class Config:
    """Торговый счет"""
    UserName = 'P077777'
    RefreshToken = '977777f3-2777-4877-8777-477777777772'

    PortfolioStocks = 'D87777'  # Фондовый рынок
    PortfolioFutures = '77778WG'  # Срочный рынок
    PortfolioFx = 'G77778'  # Валютный рынок

    Accounts = {
        PortfolioStocks: ('MOEX', 'SPBX',),  # Фондовый рынок на Московской Бирже (RUB) и СПб Бирже (USD)
        PortfolioFutures: ('MOEX',),  # Срочный рынок на Московской Бирже (RUB)
        PortfolioFx: ('MOEX',),  # Валютный рынок на Московской Бирже (RUB)
    }  # Привязка портфелей к биржам

    Boards = {
        'TQBR': (PortfolioStocks, TradeServerCode),  # Т+ Акции и ДР
        'TQOB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Гособлигации
        'TQCB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Облигации
        'RFUD': (PortfolioFutures, FutServerCode),  # FORTS: Фьючерсы
        }  # Привязка портфелей/серверов для стоп заявок к площадкам


class ConfigIIA:
    """Индивидуальный инвестиционный счет (ИИС)"""
    UserName = 'P000000'
    RefreshToken = 'ffffffff-ffff-ffff-ffff-ffffffffffff'

    PortfolioStocks = 'D00000'  # Фондовый рынок
    PortfolioFutures = '0000PSU'  # Срочный рынок
    PortfolioFx = 'G00000'  # Валютный рынок

    Accounts = {
        PortfolioStocks: ('MOEX', 'SPBX',),  # Фондовый рынок на Московской Бирже (RUB) и СПб Бирже (USD)
        PortfolioFutures: ('MOEX',),  # Срочный рынок на Московской Бирже (RUB)
        PortfolioFx: ('MOEX',),  # Валютный рынок на Московской Бирже (RUB)
    }  # Привязка портфелей к биржам

    Boards = {
        'TQBR': (PortfolioStocks, TradeServerCode),  # Т+ Акции и ДР
        'TQOB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Гособлигации
        'TQCB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Облигации
        'RFUD': (PortfolioFutures, FutServerCode),  # FORTS: Фьючерсы
    }  # Привязка портфелей/серверов для стоп заявок к площадкам


class ConfigDemo:
    """Демо счет для тестирования"""
    UserName = 'P000000'
    RefreshToken = 'ffffffff-ffff-ffff-ffff-ffffffffffff'

    PortfolioStocks = 'D00000'  # Фондовый рынок
    PortfolioFutures = '0000000'  # Срочный рынок
    PortfolioFx = 'G00000'  # Валютный рынок

    Accounts = {
        PortfolioStocks: ('MOEX', 'SPBX',),  # Фондовый рынок на Московской Бирже (RUB) и СПб Бирже (USD)
        PortfolioFutures: ('MOEX',),  # Срочный рынок на Московской Бирже (RUB)
        PortfolioFx: ('MOEX',),  # Валютный рынок на Московской Бирже (RUB)
    }  # Привязка портфелей к биржам

    Boards = {
        'TQBR': (PortfolioStocks, TradeServerCode),  # Т+ Акции и ДР
        'TQOB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Гособлигации
        'TQCB': (PortfolioStocks, TradeServerCode),  # МБ ФР: Т+: Облигации
        'RFUD': (PortfolioFutures, FutServerCode),  # FORTS: Фьючерсы
    }  # Привязка портфелей/серверов для стоп заявок к площадкам
