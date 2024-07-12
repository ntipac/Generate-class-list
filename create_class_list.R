suppressMessages(library(readr))

suppressMessages(library(dplyr))

suppressMessages(library(stringr))

suppressMessages(library(rebus))

suppressMessages(library(writexl))

  
  

#' Creates a class list from an activity file

#'

#' @param filename Path to the activity file

#'

#' @return An excel file with a class list derived from the activity file

#' @export

#'

#' @examples

#' create_class_list("activity_INB_05-23.csv")

create_class_list <- function(filename) {

  act_file <- read_csv(filename)

  

  filename_regex <- alpha(3) %R% "_" %R% digit(2) %R% "-" %R% digit(2)

  

  output_filename <- str_extract(filename, filename_regex)

  

  act_file_processed <- act_file %>%

    select(

      "user_id" = id,

      full_name,

      username,

      class_name,

      centre,

      date_joined,

      last_login

    ) %>%

    mutate(

      date_joined = as.Date(date_joined) %>% format("%Y-%h-%d")

    ) %>%

    arrange(date_joined) %>%

    mutate(

      last_login = as.Date(last_login) %>% format("%Y-%h-%d")

    ) %>%

    arrange(last_login)

  
  

  write_xlsx(act_file_processed, format_headers = FALSE, path = paste0(output_filename, ".xlsx"))

}

  
  

input_file <- commandArgs(TRUE)

  

create_class_list(input_file)
