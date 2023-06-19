import math

def enrollment_stats(value):
    data_on_enrolled = [i[1] for i in value]
    tuition_fees_data = [i[2] for i in value]



    def mean(argdata):
        avg_sum = sum(argdata) / len(argdata)
        return avg_sum

    def median(argdata):
        argdata.sort()
        if len(argdata) % 2 == 0:
            median_sum = (argdata[len(argdata) // 2 - 1] + argdata[len(argdata) // 2]) / 2
            return median_sum
        else:
            median_sum = argdata[len(argdata) // 2]
            return median_sum

    return print("*****" * 6,
                 f"\nTotal students: {sum(data_on_enrolled):,}\n"
                 f"Total tuition: $ {sum(tuition_fees_data):,}\n\n"
                 f"Student mean: {mean(data_on_enrolled):,.2f}\n"
                 f"Student median: {median(data_on_enrolled):,}\n\n"
                 f"Tuition mean: $ {mean(tuition_fees_data):,.2f}\n"
                 f"Tuition median: $ {median(tuition_fees_data):,}\n"
                 "******************************")


universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


enrollment_stats(universities)
