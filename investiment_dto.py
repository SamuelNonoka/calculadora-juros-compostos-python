class InvestimentDto:
    def __init__(self, initial_value, monthly_investment, anual_fee, period):
        self._initial_value = float(initial_value)
        self._monthly_investment = float(monthly_investment)
        self._anual_fee = float(anual_fee)
        self._period = int(period)
        self.total = 0
        
    def calc(self):
        print('\nCalculo:\n')
        
        total_fee = 0
        total_investiment = self._monthly_investment * 12
        total = self._initial_value
        month = 1
        monthly_fee = self._anual_fee / 12
        
        print(' Mês | Saldo anterior | Valor Investido | Valor em Juros | Total')
        
        while month <= self._period:
            previous_value = total
            total = previous_value + self._monthly_investment
            fee = (previous_value / 100) * monthly_fee
            
            total = total + fee
            total_fee = total_fee + fee
            
            month = self.format_print(month, 3)
            previous_value = self.format_print(round(previous_value, 2), 11)
            monthly_investment = self.format_print(round(self._monthly_investment, 2), 11)
            fee = self.format_print(round(fee, 2), 11)
                
            print(f' {month}  R$ {previous_value}  R$ {monthly_investment}  R$ {fee}  R$ {round(total, 2)}')
            
            month = int(month) + 1
            
        print(f'\nTotal: {round(total, 2)}')
        print(f'Total Investido: {round(total_investiment, 2)}')
        print(f'Juros acumulado: {round(total_fee, 2)}\n')
            
    def format_print(self, new_value, size):
        value = str(new_value)
        
        if len(value) < size:
            i = len(value)
            while i <= size:
                value = value + ' '
                i = i + 1
        
        return value    