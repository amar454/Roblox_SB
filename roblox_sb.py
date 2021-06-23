import os

skybox_files = ['sky512_bk.tex', 'sky512_dn.tex', 'sky512_ft.tex', 'sky512_lf.tex', 'sky512_rt.tex', 'sky512_up.tex']
def get_roblox_path():
    try:
        roblox_path = f'{os.getenv("LOCALAPPDATA")}\\Roblox\\Versions' 
    except:
        return None
    return roblox_path
