import snoop

cel = float(input("Enter the temperature in celcius: "))
far = float(input("Enter the temperature in far: "))


@snoop
def convert_cel_to_far(cel):
    far = (cel * 9 / 5) + 32
    return f"{far:.2f}"


def convert_far_to_cel(far):
    cel = (far - 32) * 5 / 9
    return f"{cel:.2f}"


print(convert_cel_to_far(cel))
print(convert_far_to_cel(far))
