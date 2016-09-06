#!/usr/bin/env python3
import sys
import os
import platform
import argparse
import subprocess

from .config import *
from .manual import *

def typeset_tex_file(configFilename):
    typesettingConfig = TypesettingConfig()
    if (os.path.isfile(configFilename) == True):
        typesettingConfig.set_config(configFilename)
    else:
        print(str("The config file " + configFilename + " does not exist!"))
        print("You can generate the default typesetting config with the following command:\n")
        print("    typeset.py -d your_config_file.cfg \n")
        return

    if (typesettingConfig.get_texEngine() == "pdflatex"):
        typeset_with_pdflatex(typesettingConfig)
    else:
        print(str("The TeX engine file " + typesettingConfig.get_texEngine()
            + " has not been supported yet!"))
        return

def typeset_with_pdflatex(tex2pdfConfig):
    texFilename = tex2pdfConfig.get_masterFile()
    if (os.path.isfile(texFilename) == False):
        print(str("The master TeX file " + texFilename + " does not exist!"))
        return

    outputDirectory = tex2pdfConfig.get_outputDirectory()
    print(outputDirectory)
    if (os.path.isdir(outputDirectory) == False):
        os.makedirs(outputDirectory)

    pdflatexCommand = tex2pdfConfig.get_tex2pdfCommand()
    subprocess.call(pdflatexCommand, shell = True)
    return

def generate_default_config(configFilename):
    print("The default typesetting config is written to " + configFilename + ".")
    configFile = open(configFilename, "w")
    configFile.write("# Template of typesetting config\n")

    configFile.write("\n#Master TeX file\n")
    configFile.write("master_file               = your_master_tex_file.tex\n")

    configFile.write("\n# TeX2Pdf engine\n")
    configFile.write("tex_engine                = pdflatex\n\n")

    configFile.write("\n# PdfLaTeX options\n")
    configFile.write("pdflatex_draftmode        = no\n")
    configFile.write("pdflatex_file_line_error  = yes\n")
    configFile.write("pdflatex_halt_on_error    = yes\n")
    configFile.write("pdflatex_interaction      = errorstopmode\n")
    configFile.write("pdflatex_output_directory = ./\n")
    configFile.write("pdflatex_shell_escape     = no\n")

    configFile.write("\n# Pdf viewer\n")
    configFile.write("viewer_mac                = preview\n")
    configFile.write("viewer_linux              = xdg_open\n")

    configFile.close()

def remove_nonessential_files(configFilename):
    typesettingConfig = TypesettingConfig()
    if (os.path.isfile(configFilename) == True):
        typesettingConfig.set_config(configFilename)
    else:
        print(str("The config file " + configFilename + " does not exist!"))
        return

    cleanupCommand = typesettingConfig.get_cleanupCommand()
    subprocess.call(cleanupCommand, shell = True)

def open_pdf_file(configFilename):
    typesettingConfig = TypesettingConfig()
    if (os.path.isfile(configFilename) == True):
        typesettingConfig.set_config(configFilename)
    else:
        print(str("The config file " + configFilename + " does not exist!"))
        return

    pdfFilename = typesettingConfig.get_pdfFilename()
    if (os.path.isfile(pdfFilename) == False):
        print("The pdf file " + pdfFilename + " does not exist!")
        print("Please do typesetting first!")
        return

    workingPlatform = platform.system()
    pdfViewer = typesettingConfig.get_pdf_viewer()
    if (workingPlatform == "Darwin"):
        subprocess.call(str("open -a " + pdfViewer + " " + pdfFilename), shell = True)
    elif (workingPlatform == "Linux"):
        subprocess.call(str(pdfViewer + " " + pdfFilename + " &"), shell = True)

    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--clean", nargs='?', type=str, const="typeset.cfg",
        metavar="typesetting_config_filename",
        help="Clean all nonessential files except the pdf ones")
    parser.add_argument("-d", "--default", nargs='?', type=str, const="typeset.cfg",
        metavar="typesetting_config_filename",
        help="Generate the default typeset config file")
    parser.add_argument("-m", "--manual", action="store_true", help="Show the manual")
    parser.add_argument("-o", "--open", nargs='?', type=str, const="typeset.cfg",
        metavar="typesetting_config_filename",
        help="Open the PDF file")
    parser.add_argument("-t", "--typeset", nargs='?', type=str, const="typeset.cfg",
        metavar="typesetting_config_filename",
        help="Typeset a TeX file")

    args = parser.parse_args()

    if (args.typeset):
        typeset_tex_file(str(args.typeset).strip())

    if (args.manual):
        print_manual()

    if (args.default):
        generate_default_config(str(args.default).strip())

    if (args.clean):
        remove_nonessential_files(str(args.clean).strip())

    if (args.open):
        open_pdf_file(str(args.open).strip())

    return
