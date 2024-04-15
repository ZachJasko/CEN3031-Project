options(scipen = 9999)
library(openxlsx)
library(tidyverse)
library(generator)
library(qdap)

names_many <- generator::r_full_names(5000000)

name <- sample(names_many[!duplicated(names_many)],size = 100)   

phone_many <- generator::r_phone_numbers(1000000, use_hyphens = TRUE)

phone <- sample(phone_many[!duplicated(phone_many)],size = 100) 


pre_address <- openxlsx::read.xlsx("Profile_Additional Details\\Profile_Additional Details.xlsx")

email <- paste0(gsub("[[:punct:]]", "", paste0(tolower(gsub("^(.*?),.*", "\\1", name)),
                                               tolower(strtrim(sub('.*,\\s*', '', name), 1)))), "@ufl.edu")

cities <- sample(rep(c("Jacksonville",
                       "Tallahassee",
                       "Miami",
                       "Orlando",
                       "St Petersburg",
                       "Tampa",
                       "Fort Lauderdale",
                       "Clearwater",
                       "Hialeah",
                       "Hollywood",
                       "Coral Springs",
                       "Cape Coral",
                       "Daytona Beach"), 5000000), size = 100)


userids_many <- paste0(sample(1111:9999, 8888), "-", sample(1111:9999, 8888))
  
userids <- sample(userids_many[!duplicated(userids_many)],size = 100)   

sex <- as.character(head(qdap::name2sex(gsub( " .*$", "", name)), -2))

gator_points <- sample(rep(1:500, 5000), 100)


dob <- sample(rep(seq(as.Date('1990/01/01'), as.Date('2003/12/31'), 
                      by=paste0(sample(1:60, 1), " day")), 30000),
              size = 100)


password <- rep("12345", 100)

pronouns <- ifelse(sex == "M", "He/Him", "She/Her")

idx <- sample(1:100, 25)

pronouns[idx] <- "They/Them"

age <- as.numeric(format(as.Date(Sys.Date()),"%Y")) - as.numeric(format(as.Date(dob),"%Y"))


academicLevel_many <- c("freshman", "sophomore", "junior", "senior")
  
idx <- paste(academicLevel_many, collapse="|")

student_year <- stringr::str_to_title(stringr::str_extract(pre_address$Bios, idx))

academicLevel_many <- sample(rep(c("Freshman", "Sophomore", "Junior", "Senior"), 100), size = 100)

student_year[is.na(student_year)] <- sample(academicLevel_many, sum(is.na(student_year)), replace = TRUE)


profile_pics_links <- sample(rep(c("https://drive.google.com/file/d/1xmfvDL7C80xVUfmwh4unUKnur3KMM9aP/view?usp=drive_link",
                        "https://drive.google.com/file/d/1Ur9H9bRcoPL3-Rmuj9mmxPbUqcw9AvS5/view?usp=drive_link",
                        "https://drive.google.com/file/d/14DBRX17WcdnJNFvBmwzpqO31PHLxNi_u/view?usp=drive_link",
                        "https://drive.google.com/file/d/1QnTvtQvHMEXtaQnFZbokJu6godzQcMv3/view?usp=drive_link",
                        "https://drive.google.com/file/d/1keeE7M1jyBA0b_4H0Rlov18P5k7azVDP/view?usp=drive_link",
                        "https://drive.google.com/file/d/1-ceInSo-5cerM-nCC8PTjQyxSxGfgCSi/view?usp=drive_link",
                        "https://drive.google.com/file/d/1Zij9Vtm3sTzQKiqYzxSPqmLF8SeLQkiY/view?usp=drive_link",
                        "https://drive.google.com/file/d/1ODQZQ6u0RNNdU19JNyryo5LARdLEWacf/view?usp=drive_link",
                        "https://drive.google.com/file/d/1jjFOxOF6ZHdEPpJb9kbfvbpyr0zOQV-8/view?usp=drive_link",
                        "https://drive.google.com/file/d/1m0DZAPh7HlDLD3Tvd9KaX26ukuiNim5T/view?usp=drive_link",
                        "https://drive.google.com/file/d/1w73-AtGzEdOH6_OOGFg7mCkeJP7oNehQ/view?usp=drive_link",
                        "https://drive.google.com/file/d/1LPIRBrhW9BuNV5XCeojt7OzvmVcQd15P/view?usp=drive_link",
                        "https://drive.google.com/file/d/1ZE-XxZ_8Z1BJ50-pAsE03YIQblC3YCXq/view?usp=drive_link",
                        "https://drive.google.com/file/d/18NdgJ7OF73weG0pRkFzNxJd9KhRIPdFc/view?usp=drive_link",
                        "https://drive.google.com/file/d/1TR7SkXg9-Zy4N0BUbOESvSiozTO_xaMk/view?usp=drive_link",
                        "https://drive.google.com/file/d/1e3imLsLJEFf-cZnfVFXWf_8ZyLU7zFmr/view?usp=drive_link",
                        "https://drive.google.com/file/d/1xYSXiIJNv-dLf7cmLg14-dax46W1YkUh/view?usp=drive_link"), 1000), 100)

profile_level <- ifelse(gator_points >= 0 & gator_points <= 100, 1,
                        ifelse(gator_points >= 101 & gator_points <= 200, 2, 
                               ifelse(gator_points >= 201 & gator_points <= 300, 3,
                                      ifelse(gator_points >= 301 & gator_points <= 400, 4,
                                             ifelse(gator_points >= 401 & gator_points <= 500, 5, 6)))))

profile_badges <- ifelse(profile_level == 1, "https://drive.google.com/file/d/1N0xZRCEgMDjRopQa8xzZRfWBgzZHnfn_/view?usp=drive_link",
                         ifelse(profile_level == 2, "https://drive.google.com/file/d/1-S1BjowxmH5OVU6ZvKQyD8iNUZGmoRW0/view?usp=drive_link", 
                                ifelse(profile_level == 3, "https://drive.google.com/file/d/1ZT3PG5S4lLqcrgVo_mXIBbIYOVCTLzMd/view?usp=drive_link",
                                       ifelse(profile_level == 4, "https://drive.google.com/file/d/1ebBQZTVlTjTl9o59v5h1VrHf3bkqZPcd/view?usp=drive_link",
                                              ifelse(profile_level == 5, "https://drive.google.com/file/d/1X-iVMP3lMh6DjcEqzrtlcVRTzOBVtSdZ/view?usp=drive_link",
                                                     "https://drive.google.com/file/d/1su7cj-_C43KALBmf91kM3W6-7fGPgjxJ/view?usp=drive_link")))))
  

fake_dataframe <- data.frame(profile_full_name = name,
                             profile_phone = phone,
                             profile_email = email,
                             profile_id = userids,
                             profile_street_address = pre_address$StreetAddress,
                             profile_address_city = cities,
                             profile_address_state = pre_address$StateFull,
                             profile_address_zip = pre_address$ZipCode,
                             profile_bios = pre_address$Bios,
                             profile_password = password,
                             profile_gatorpts = gator_points,
                             profile_level = profile_level,
                             profile_lvlbadges_links = profile_badges,
                             profile_photo = profile_pics_links,
                             profile_academic_year = student_year,
                             profile_sex = sex,
                             profile_prefers_pronoun = pronouns,
                             profile_dob = dob,
                             profile_age = age
                  )


openxlsx::write.xlsx(fake_dataframe, "fake_swampService_data.xlsx")
