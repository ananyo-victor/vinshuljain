for i in range(2,21):
    with open(f"table/multiplication_table {i}","w") as f:
        for a in range(11):
            f.white(f"{i}x{a}={i*a}\n")
