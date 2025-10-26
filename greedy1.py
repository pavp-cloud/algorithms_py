#есть мероприятия на фестивале кодируются 2-мя числами время начала и время конца
#дан список таких мероприятий с таким кодированием
#необходимо так их распределить чтобы попасть на наибольшее кол-во мероприятий



def fest(events):
    sorted = events.copy()
    sorted.sort(key=lambda tup: tup[1])  # sorts in place
    complete = []
    last_time = 0
    for i in sorted:
        if last_time <= i[0]:
            complete.append(i)
            last_time = i[1]
    return complete





def main():
    assert fest([(1, 2), (1, 4), (3, 4), (5, 6)]) == [(1, 2), (3, 4), (5, 6)]
    assert fest([(5,6), (1,2), (3,4)]) == [(1,2), (3,4), (5,6)]
    assert fest([(1,2)]) == [(1,2)]
    assert fest([(1, 25), (10, 20), (10, 30), (30, 40), (50, 60)]) == [(10, 20), (30,40), (50,60)]
if __name__ == '__main__':
    main()