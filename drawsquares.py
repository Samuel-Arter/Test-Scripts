# print("+---" * 3)
def draw_n_squares(n):
    top_footer = "+---" * n + "+"
    middle = "|   " * n + "|"
    output = []

    for _ in range(n):
        output.append(top_footer)
        output.append(middle)

    output.append(top_footer)

    return "\n".join(output)



# Example usage:
print(draw_n_squares(5))