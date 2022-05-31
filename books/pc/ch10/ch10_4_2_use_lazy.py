import ch10_4_2_module_lazy


if __name__ == "__main__":
    a = ch10_4_2_module_lazy.A()
    a.spam()

    print(isinstance(a, ch10_4_2_module_lazy.a.A))
