#Я не смогла сделать это задание сама, потому тут разобирала Ваши решения что бы понять
def task_3():
    wages = {}
    try:
        with open('workers_file', 'r', encoding='utf-8') as f:
            for line in f:
                wages[line.split()[0]] = float(line.split()[1])
        print ("Wage below 20000:")
        for name, wage in wages.items():
            if wage < 20000:
                print (name)
        print(f'Awerage salary = {sum(wages.values())/len(wages)}')
    except IOError:
        print('Fatality')
    except:
        print('Error')


task_3()
