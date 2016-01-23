HOST = "irc.twitch.tv"
PORT = 6667
PASS = "oauth:ldms5nepxaum2eq6mrf75txsi8ajr6"
IDENT = "nerfsbot"
CHANNEL = "nerfireliapls"
ircPASS = str.encode("PASS " + PASS + "\r\n")
ircIDENT = str.encode("NICK " + IDENT + "\r\n")
ircCHANNEL = str.encode(("JOIN #" + CHANNEL + "\r\n"))
