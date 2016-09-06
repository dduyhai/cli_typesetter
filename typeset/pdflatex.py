import os

class PdfLatex:
    def __init__(self):
        self.draftmode = False
        self.fileLineError = True
        self.haltOnError = True
        self.interaction = "errorstopmode"
        self.outputDirectory = "."
        self.shellEscape = False

    def set_option(self, optionName, optionValue):
        localOption = str(optionName).lower();
        if (localOption == "pdflatex_draftmode"):
            self.set_draftmode(optionValue)
        elif (localOption == "pdflatex_file_line_error"):
            self.set_fileLineError(optionValue)
        elif (localOption == "pdflatex_halt_on_error"):
            self.set_haltOnError(optionValue)
        elif (localOption == "pdflatex_interaction"):
            self.set_interaction(optionValue)
        elif (localOption == "pdflatex_output_directory"):
            self.set_outputDirectory(optionValue)
        elif (localOption == "pdflatex_shell_escape"):
            self.set_shellEscape(optionValue)

    def set_draftmode(self, draftmodeValue):
        localValue = str(draftmodeValue).lower()
        if ((localValue == "true") or (localValue == "yes") or (localValue == "enable")):
            self.draftmode = True
        elif ((localValue == "false") or (localValue == "no") or (localValue == "disable")):
            self.draftmode = False

    def set_fileLineError(self, fileLineErrorMode):
        localValue = str(fileLineErrorMode).lower()
        if ((localValue == "true") or (localValue == "yes") or (localValue == "enable")):
            self.fileLineError = True
        elif ((localValue == "false") or (localValue == "no") or (localValue == "disable")):
            self.fileLineError = False

    def set_haltOnError(self, haltOnErrorMode):
        localValue = str(haltOnErrorMode).lower()
        if ((localValue == "true") or (localValue == "yes") or (localValue == "enable")):
            self.haltOnError = True
        elif ((localValue == "false") or (localValue == "no") or (localValue == "disable")):
            self.haltOnError = False

    def set_interaction(self, interactionMode):
        localValue = str(interactionMode).lower()
        if ((localValue == "batchmode") or (localValue == "nonstopmode")
            or (localValue == "scrollmode") or (localValue == "errorstopmode")):
            self.interaction = localValue

    def set_outputDirectory(self, directory):
        if (directory != ""):
            self.outputDirectory = os.path.expandvars(os.path.expanduser(directory))

    def set_shellEscape(self, shellEscapeMode):
        localValue = str(shellEscapeMode).lower()
        if ((localValue == "true") or (localValue == "yes") or (localValue == "enable")):
            self.shellEscape = True
        elif ((localValue == "false") or (localValue == "no") or (localValue == "disable")):
            self.shellEscape = False

    def export_command(self, texFileName):
        command = str("texfot pdflatex"
            + " -interaction=" + self.interaction
            + " %O %S")
        if (self.draftmode):
            command = str(command + " -draftmode")
        if (self.fileLineError):
            command = str(command + " -file-line-error")
        if (self.haltOnError):
            command = str(command + " -halt-on-error")
        if (self.shellEscape):
            command = str(command + " -shell-escape")
        # command = str(command + " " + texFileName)
        command = str("latexmk -pdf"
            + " -outdir=" + self.outputDirectory
            + " -pdflatex=" + "\"" + command + "\""
            + " " + texFileName)
        return command
