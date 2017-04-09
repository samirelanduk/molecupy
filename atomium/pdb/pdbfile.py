class PdbRecord:
    """A PdbRecord represents a single line in a PDB file. As such, it follows
    the same constraints that the PDB file formats impose on the lines in the
    actual files - namely that it cannot be more than 80 characters.

    :param str text: The string contents of the line in the PDB file.
    :raises ValueError: if a string longer than 80 characters is supplied."""

    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("PdbRecord needs str, not '%s'" % str(text))
        if len(text) > 80:
            raise ValueError("'%s' is longer than 80 characters" % str(text))
        self._text = text


    def text(self, text=None):
        """The full string of the record. If a string is passed as an argument,
        the text will be updated.

        :param str text: If given, the record's text will be updated to this.
        :raises ValueError: if a string longer than 80 characters is supplied."""

        if text is None:
            return self._text
        else:
            if not isinstance(text, str):
                raise TypeError("PdbRecord needs str, not '%s'" % str(text))
            if len(text) > 80:
                raise ValueError("'%s' is longer than 80 characters" % str(text))
            self._text = text


    def name(self, name=None):
        """The name of the record, given by the first six characters of the line
        in the PDB file. The name will have any whitespace removed. If a string
        is passed as an argument, the name will be updated.

        :param str name: If given, the record's name will be updated to this.
        :raises ValueError: if a string longer than 6 characters is supplied."""

        if name is None:
            return self._text[:6].strip()
        else:
            if not isinstance(name, str):
                raise TypeError("PdbRecord needs str, not '%s'" % str(name))
            if len(name) > 6:
                raise ValueError("'%s' is longer than 6 characters" % str(name))
            self._text = name + (" " * (6 - len(name))) + self._text[6:]
