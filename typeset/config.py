import os
import platform

from .pdflatex import *

# import bibtex

class Option:
    def __init__(self):
        self.type = "Unknown type"
        self.name = "Unknown name"
        self.value = "Unknown value"

def extract_option(optionCommand):
    opt = Option()
    commandElements = (str(optionCommand)).split()
    if (len(commandElements) < 3):
        return opt
    if (commandElements[1] != "="):
        return opt
    opt.name = str(commandElements[0]).strip()
    opt.value = commandElements[2]
    opt.type = commandElements[0].split("_")[0]
    return opt

class TypesettingConfig:
    def __init__(self):
        self.masterFile = ""
        self.texEngine = "pdflatex"
        self.pdflatexOption = PdfLatex()
        self.macPdfViewer = "preview"
        self.linuxPdfViewer = "xdg-open"
        # self.xelatexOption = xelatex.XeLatex()
        # self.bibEngine = "bibtex"
        # self.bibtexOption = bibtex.BibTex()

    def set_config(self, configFilename):
        if (os.path.isfile(configFilename) == False):
            print("The config file is not found!")
            return
        configFilestream = open(configFilename)
        while (True):
            line = configFilestream.readline()
            if (not line):
                break
            line = str(line).strip()
            if ((len(line) == 0) or (line[0] == "#")):
                continue
            configOption = extract_option(line)
            if (configOption.type == "master"):
                self.masterFile = configOption.value
            elif (configOption.type == "tex"):
                self.texEngine = configOption.value
            elif (configOption.type == "pdflatex"):
                self.pdflatexOption.set_option(configOption.name, configOption.value)
            elif (configOption.type == "viewer"):
                self.set_pdf_viewer(configOption.name, configOption.value)

    def set_pdf_viewer(self, workingPlatform, pdfViewer):
        if (workingPlatform == "viewer_mac"):
            self.macPdfViewer = pdfViewer
        elif (workingPlatform == "viewer_linux"):
            self.linuxPdfViewer = pdfViewer

    def get_pdf_viewer(self):
        workingPlatform = platform.system()
        if (workingPlatform == "Darwin"):
            return self.macPdfViewer
        elif (workingPlatform == "Linux"):
            return self.linuxPdfViewer

    def get_texEngine(self):
        return self.texEngine

    def get_masterFile(self):
        return self.masterFile

    def get_outputDirectory(self):
        if (self.texEngine == "pdflatex"):
            outputDirectory = self.pdflatexOption.outputDirectory
            return outputDirectory

    def get_tex2pdfCommand(self):
        if (self.texEngine == "pdflatex"):
            return self.pdflatexOption.export_command(self.masterFile)

    def get_cleanupCommand(self):
        cleanupCommand = str("latexmk -c -outdir=" + self.get_outputDirectory())
        return cleanupCommand

    def get_pdfFilename(self):
        pdfFilename = ""
        lengthOfMasterFilename = len(self.masterFile)
        if (lengthOfMasterFilename > 4):
            extensionOfMasterFilename = self.masterFile[(lengthOfMasterFilename - 4) : lengthOfMasterFilename]
            if (extensionOfMasterFilename == ".tex"):
                pdfFilename = str(self.masterFile[0 : (lengthOfMasterFilename - 4)] + ".pdf")
            else:
                pdfFilename = str(self.masterFile + ".pdf")
        else:
            pdfFilename = str(self.masterFile + ".pdf")
        pdfFilename = self.get_outputDirectory() + "/" + pdfFilename
        return pdfFilename
