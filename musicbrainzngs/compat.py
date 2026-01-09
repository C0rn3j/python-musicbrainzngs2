from http.client import BadStatusLine, HTTPException
from io import StringIO
from urllib.error import HTTPError, URLError
from urllib.parse import quote_plus, urlencode, urlunparse
from urllib.request import HTTPDigestAuthHandler, HTTPHandler, HTTPPasswordMgr, Request, build_opener
