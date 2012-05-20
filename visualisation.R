# Let's consider all the results
files <- c('get_thread_length', 'get_email', 'first_email_in_archives_range',
    'get_thread_length','get_thread_participants', 'get_archives_length',
    'get_archives_range', 'get_list_size',
    'search_subject', 'search_content', 'search_content_subject', 'search_sender',
    'search_subject_cs', 'search_content_cs', 'search_content_subject_cs',
    'search_sender_cs')

# We want to have an overview of how well the two databases systems are
# doing compare to each other.
# For Postgresql we include the comparison of using a union of queries
# vs using a or statement.

png('overview.png', width = 1500, height = 1500, units = "px", pointsize = 20,)
par(mfrow = c(4, 4), pty = "s")
for (filename in files){
    tmp <- read.table(file=filename, sep='\t', header=T)
    boxplot(tmp, main=filename, ylab='Time in s',
        col=(c("gold","darkgreen","green")), log='y')
}
dev.off()

png('overview_simplified.png', width = 1500, height = 1500, units = "px", pointsize = 20,)
par(mfrow = c(4, 4), pty = "s")
for (filename in files){
    tmp <- read.table(file=filename, sep='\t', header=T)
    boxplot(tmp, main=filename, ylab='Time in s',
        col=(c("gold","darkgreen","green")), log='y', outline=F)
}
dev.off()

# Now we're going to use only the search results
files <- c(
    c('search_subject', 'search_subject_cs'),
    c('search_content', 'search_content_cs'),
    c('search_content_subject', 'search_content_subject_cs'),
    c('search_sender', 'search_sender_cs')
    )


# We want to compare within a database system the speed of case sensitive
# queries vs case insensitive queries.

png('mg_sensitivity.png', width = 700, height = 700, units = "px", pointsize = 12,)
par(mfrow = c(2, 2), pty = "s")
i <- 1
while (i < length(files)){
#    print(i)
    tmp <- read.table(file=files[i], sep='\t', header=T)
    tmp2 <- read.table(file=files[i + 1], sep='\t', header=T)
    tmp <- cbind(tmp[,"MG"], tmp2[,"MG"])
    colnames(tmp) <- c("MG", "MG-CS")
    boxplot(tmp, main=files[i], ylab='Time in s',
        col=(c("gold","darkgreen","green")), log='y', outline=F)
    i <- i + 2
}
dev.off()

png('pg_sensitivity.png', width = 700, height = 700, units = "px", pointsize = 12,)
par(mfrow = c(2, 2), pty = "s")
i <- 1
while (i < length(files)){
#    print(i)
    tmp <- read.table(file=files[i], sep='\t', header=T)
    tmp2 <- read.table(file=files[i + 1], sep='\t', header=T)
    if ("PG.or" %in% colnames(tmp)){
        tmp[,"PG"] <- tmp[,"PG.or"]
    }
    if ("PG.or" %in% colnames(tmp2)){
        tmp2[,"PG"] <- tmp2[,"PG.or"]
    }
    tmp <- cbind(tmp[,"PG"], tmp2[,"PG"])
    colnames(tmp) <- c("PG", "PG-CS")
    boxplot(tmp, main=files[i], ylab='Time in s',
        col=(c("gold","darkgreen","green")), log='y', outline=F)
    i <- i + 2
}
dev.off()
