import ptcgcl
from GUI import gui_main
import ptcgcl.Build_Deck

ptcgcl.Board_changer.Board_CL()[ptcgcl.Board_changer.Board_CL().board_dic.index("POKEMON_SC_1"), 0, "PARALYZED"] = 1
print(ptcgcl.Board_changer.Board_CL()[ptcgcl.Board_changer.Board_CL().board_dic.index("POKEMON_SC_1")])



