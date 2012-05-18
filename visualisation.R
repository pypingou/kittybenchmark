
files <- c('get_thread_length', 'get_email', 'first_email_in_archives_range',
    'get_thread_length', 'get_archives_length', 'search_subject',
    'search_content', 'search_content_subject', 'get_list_size')

dataset <- data.frame()
for (filename in files){
    tmp <- read.table(file=filename, sep='\t', header=T)
    colnames(tmp) <- c('pg', 'mg')
    if (length(dataset) == 0){
        dataset <- tmp
    } else {
        dataset <- cbind(dataset, tmp)
    }
}

boxplot(dataset, main='benchmark', ylab='Time in s',
    col=(c("gold","darkgreen")), log='y')

png('overview.png', width = 1600, height = 1600, units = "px", pointsize = 48,)
par(mfrow = c(3, 3), pty = "s")
for (filename in files){
    tmp <- read.table(file=filename, sep='\t', header=T)
    colnames(tmp) <- c('pg', 'mg')
    boxplot(tmp, main=filename, ylab='Time in s',
        col=(c("gold","darkgreen")), log='y')
}
dev.off()

png('overview_simplified.png', width = 1600, height = 1600, units = "px", pointsize = 48,)
par(mfrow = c(3, 3), pty = "s")
for (filename in files){
    tmp <- read.table(file=filename, sep='\t', header=T)
    colnames(tmp) <- c('pg', 'mg')
    boxplot(tmp, main=filename, ylab='Time in s',
        col=(c("gold","darkgreen")), log='y', outline=F)
}
dev.off()


#png('get_email.png')
boxplot(dataset, main='benchmark', ylab='time in s')
#dev.off()
