# Mod Skeleton Creator
# Made by DeBeast591
# Enjoy!

import shutil
import os
import tkinter as tk

def callback():
    global namespace_name, display_name
    shutil.copytree("./template/", "./" + namespace_name.get() + "/")
    with open("./" + namespace_name.get() + "/" + namespace_name.get() + ".cs", "w+") as MainModFile:
        MainModFile.writelines(["using Terraria.ModLoader;\n",
                                "\n",
                                "namespace " + namespace_name.get() + " {\n",
                                "   public class " + namespace_name.get() + " : Mod {\n",
                                "       public " + namespace_name.get() + "() {}\n",
                                "   }\n",
                                "}\n"])
        MainModFile.close()

    with open("./" + namespace_name.get() + "/" + namespace_name.get() + ".csproj", "w+") as CsprojModFile:
        CsprojModFile.writelines(["<?xml version=\"1.0\" encoding=\"utf-8\"?>\n",
                                   "<Project Sdk=\"Microsoft.NET.Sdk\">\n",
                                       "<Import Project=\"..\..\references\tModLoader.targets\" />\n",
                                       "<PropertyGroup>\n",
                                           "<AssemblyName>" + namespace_name.get() + "</AssemblyName>\n",
                                           "<TargetFramework>net45</TargetFramework>\n",
                                           "<PlatformTarget>x86</PlatformTarget>\n",
                                           "<LangVersion>latest</LangVersion>\n",
                                       "</PropertyGroup>\n",
                                       "<Target Name=\"BuildMod\" AfterTargets=\"Build\">\n",
                                           "<Exec Command=\"&quot;$(tMLBuildServerPath)&quot; -build $(ProjectDir) -eac $(TargetPath) -define $(DefineConstants) -unsafe $(AllowUnsafeBlocks)\" />\n",
                                       "</Target>\n",
                                   "</Project>\n"])
        CsprojModFile.close()

    with open("./" + namespace_name.get() + "/description.txt", "w") as DescFile:
        DescFile.write(display_name.get() + " is a pretty cool mod, it does...this. Modify this file with a description of your mod.")
        DescFile.close()

    with open("./" + namespace_name.get() + "/build.txt", "w") as BuildFile:
        BuildFile.writelines(["displayName = " + display_name.get() + "\n",
                              "author = " + author_name.get() + "\n",
                              "verion = 0.1\n"])
        BuildFile.close()

    print("Done!")
    exit()

window = tk.Tk()

title = tk.Label(window, text="Mod Skeleton Creator")

namespace_name_text = tk.Label(window, text="Mod Name (No Spaces)").grid(row=0)
namespace_name = tk.Entry(window)
namespace_name.grid(row=0, column=1)

display_name_text = tk.Label(window, text="Mod Display Name").grid(row=1)
display_name = tk.Entry(window)
display_name.grid(row=1, column=1)

author_text = tk.Label(window, text="Author's Name").grid(row=2)
author_name = tk.Entry(window)
author_name.grid(row=2, column=1)

make_mod_button = tk.Button(window, text="Done", command=lambda: callback())
make_mod_button.grid(row=3, column=1)

cancel = tk.Button(window, text="Exit", command=lambda: exit())
cancel.grid(row=3, column=0)

window.mainloop()
