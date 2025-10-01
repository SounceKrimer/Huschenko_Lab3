from translator_pkg import deep_ld_mod as d3

if __name__ == "__main__":
    sample = "Hallo, wie geht es dir?"
    print("LangDetect (all):", d3.LangDetect(sample, "all"))
    print("Translate to en:", d3.TransLate(sample, "auto", "en"))
    print("CodeLang('german') ->", d3.CodeLang("german"))
    d3.LanguageList("screen", sample)
    