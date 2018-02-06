records <- read.csv("out/vvb_chat_hist.csv")
# remove empty rows
records <- na.omit(records)

amount <- length(records)
# format rectime
records$RECTIME <- strptime(records$RECTIME, "%y-%m-%d %H:%M:%S")

# count_by_date_range <- function(from, to) {
#   print(subset(records, records$RECTIME >= "2013-11-01 16:14:28"))
# }

count_by_nick <- function(nick) {
  nrow(subset(records, records$NICK == nick))
}
# Main workflow #
count_by_nick("?")
count_by_nick("?")
# plot(count_by_nick("?"), 
#      count_by_nick("?"))
