class Personal():
    def __init__(self,name):
        print(f'{name}이 생성 되었습니다.')
        
    def print_record(self,name):
        print(f'생성된 사람이름은 {name}입니다.')

h1 = Personal('Justin')
h1.print_record()


