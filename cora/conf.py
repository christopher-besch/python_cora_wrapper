from jinja2 import Environment, FileSystemLoader


# class with every global variable for the config file
class GlobalObj:
    des_mod = "Default Global"
    des_glo = "Made by Python cora wrapper"

    # global settings to define the interval of evaluation
    a_thres = 0.03
    b_thres = 0.075
    a_eval = 0.01
    b_delta_end = 0.2
    t_min = "automatic"
    t_max = "automatic"

    # global settings of the corridor method
    k = 2
    g_1 = 0.5
    a_0 = 0.05
    b_0 = 0.5
    a_sigma = 0
    b_sigma = 0

    # global settings of the cross correlation method
    d_min = 0.01
    d_max = 0.12
    int_min = 0.8
    k_v = 10
    k_g = 1
    k_p = 1
    g_v = 0.5
    g_g = 0.25
    g_p = 0.25
    g_2 = 0.5

    # normalisation of the the weighting factors
    wf_norm = "YES"

    # signal settings
    isoname_1_2 = "YES"
    isoname_11_12 = "YES"
    min_norm = 0
    y_norm = "extremum"

    # format settings of the html report
    output_format = "Hypergraph"

    # layout of the html report
    font_small = 12
    font_large = 14
    pret_lc = -1
    postt_lc = -1

    load_cases = []

    def add_load_case(self):
        next_idx = len(self.load_cases)
        self.load_cases.append(LoadCase(f"Load Case #{next_idx}"))


# derivative of GlobalObj
class LoadCase(GlobalObj):
    method = "cora"

    sub_load_cases = []

    data_files = []
    signals = []

    def __init__(self, name):
        self.nam_lc = name
        self.des_lc = "Made by Python cora wrapper"
        self.wf_lc = 1

    def add_sub_load_case(self):
        next_idx = len(self.sub_load_cases)
        self.sub_load_cases.append(SubLoadCase(f"Sub Load Case #{next_idx}"))

    def add_data_file(self, file):
        self.data_files.append(DataFile(file))

    def add_signal(self, curve):
        self.signals.append(Signal(curve))


class SubLoadCase(LoadCase):
    data_files = []
    signals = []

    def __init__(self, name):
        self.nam_scl = name
        self.des_scl = "Made by Python cora wrapper"
        self.wf_scl = 1


class DataFile:
    def __init__(self, file):
        self.name = file
        self.timeshift = 0
        self.unit = "m-Kg-s"
        self.g = "NO"


class Signal(GlobalObj):
    def __init__(self, curve):
        self.name = curve
        self.wf = 1
        self.a_t = "NOTSPEC"
        self.filter = 0


def write(global_obj):
    # create jinja2 environment
    # location of the templates folder
    jinja_env = Environment(loader=FileSystemLoader("cora\\config_template"))
    # get main template
    template = jinja_env.get_template("global.jinja")

    text = ""

    for line in template.render(global_obj=global_obj).split("\n"):
        if line.strip() != "":
            print(line.strip())
            text += line.strip() + "\n"

    with open("C:\\Users\\Stromel\\Desktop\\test\\conf.cps", "w", encoding="utf-8") as file:
        file.write(text)
