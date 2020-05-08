from cora import write, GlobalObj

global_obj = GlobalObj()
global_obj.add_load_case()

global_obj.load_cases[0].add_data_file("C:\\Users\\Stromel\\Downloads\\CORAplus404complete_170621(1)\\examples\\standard\\data\\loadcase_01\\iso\\test_01.iso")
global_obj.load_cases[0].add_data_file("C:\\Users\\Stromel\\Downloads\\CORAplus404complete_170621(1)\\examples\\standard\\data\\loadcase_01\\iso\\test_02.iso")
global_obj.load_cases[0].add_data_file("C:\\Users\\Stromel\\Downloads\\CORAplus404complete_170621(1)\\examples\\standard\\data\\loadcase_01\\iso\\test_03.iso")
global_obj.load_cases[0].add_data_file("C:\\Users\\Stromel\\Downloads\\CORAplus404complete_170621(1)\\examples\\standard\\data\\loadcase_01\\iso\\test_04.iso")
global_obj.load_cases[0].add_data_file("C:\\Users\\Stromel\\Downloads\\CORAplus404complete_170621(1)\\examples\\standard\\data\\loadcase_01\\iso\\cae_01.iso")

global_obj.load_cases[0].add_signal("S1SENS010000DS0D")
global_obj.load_cases[0].add_signal("S1SENS020000FO0D")
global_obj.load_cases[0].add_signal("S1SENS030000ACXA")
global_obj.load_cases[0].add_signal("S1SENS030000ACYA")
global_obj.load_cases[0].add_signal("S1SENS030000ACZA")
global_obj.load_cases[0].add_signal("S1SENS040000FOXA")
global_obj.load_cases[0].add_signal("S1SENS040000FOYA")
global_obj.load_cases[0].add_signal("S1SENS040000FOZA")
global_obj.load_cases[0].add_signal("S1SENS040000MOXB")
global_obj.load_cases[0].add_signal("S1SENS040000MOYB")
global_obj.load_cases[0].add_signal("S1SENS040000MOZB")
global_obj.load_cases[0].add_signal("S1SENS050000DSXC")

write(global_obj)
