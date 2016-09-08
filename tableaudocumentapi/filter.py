###############################################################################
#
# Connection - A class for writing connections to Tableau files
#
###############################################################################


class Filter(object):
    """
    A class for writing filters to Tableau files.

    """

    ###########################################################################
    #
    # Public API.
    #
    ###########################################################################

    def __init__(self, filterxml):
        """
        Constructor.

        """
        self._filterXML = filterxml
        self._type = filterxml.get('class')
        self._column = filterxml.get('column')
        self._filtergroup = filterxml.get('filter-group')

        self._member = self._find_group_filter().get('member')

    def __repr__(self):
        return "<Filter type='{}' column='{}' member='{}'>".format(
            self._type, self._column, self._member
        )

    ###########
    # class
    ###########
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self._connectionXML.set('type', value)

    ###########
    # column
    ###########
    @property
    def column(self):
        return self._server

    @column.setter
    def column(self, value):
        self._column = value
        self._connectionXML.set('column', value)

    ###########
    # member
    ###########
    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, value):
        self._member = value
        self._find_group_filter().set('member', value)

    def _find_group_filter(self):
        return self._filterXML.find('groupfilter')
