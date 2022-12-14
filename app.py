from investiment_dto import InvestimentDto

def run_app():
    print('*** CALCULADORA DE CUSTOS***\n')
    
    investiment = get_investiment()
    investiment.calc()
    
def get_investiment():
    _initial_value = ask_value('Informe o valor inicial: ')
    _monthly_investment = ask_value('Informe qual será seu investimento mensal: ')
    _anual_fee = ask_value('Informe a taxa de juros anual: ')
    _period = ask_value('Informe quanto tempo deseja investir em meses: ')
    
    return InvestimentDto(_initial_value, _monthly_investment, _anual_fee, _period)
    
def ask_value(question):
    value = input(question)
    
    if value.isnumeric() or isinstance(25.9, float):
        return value
    
    print('Informe um valor válido')
    return ask_value(question)
        
if __name__ == '__main__':
    run_app()
    