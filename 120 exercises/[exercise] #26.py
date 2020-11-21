def histograma(items):
    for n in items:
        output = ''
        times = n
        while(times > 0):
            output += '*'
            times = times - 1
            print(output)

histograma([2,3,6,5])