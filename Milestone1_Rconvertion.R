# Generate a list of workers
generate_workers <- function(num_workers) {
  workers <- list()
  for (i in 1:num_workers) {
    name <- paste0("NXU Staff ", sample(1:503, 1))
    salary <- sample(5000:35000, 1)
    gender <- sample(c("Male", "Female"), 1)
    worker <- list(name = name, salary = salary, gender = gender)
    workers[[i]] <- worker
  }
  return(workers)
}

# Generate payment slips
generate_payment_slips <- function(workers) {
  payment_slips <- list()
  for (worker in workers) {
    name <- worker$name
    salary <- worker$salary
    gender <- worker$gender
    
    if (salary > 10000 & salary < 20000) {
      employee_level <- "A1"
    } else if (salary > 7500 & salary < 30000 & gender == "Female") {
      employee_level <- "A5-F"
    } else {
      employee_level <- "No Level"
    }
    
    payment_slip <- paste0("Name: ", name, ", Salary: $", format(salary, nsmall = 2), ", Employee Level: ", employee_level)
    payment_slips[[length(payment_slips) + 1]] <- payment_slip
  }
  return(payment_slips)
}

# Main execution
num_workers <- 503
workers <- generate_workers(num_workers)
payment_slips <- generate_payment_slips(workers)

for (slip in payment_slips) {
  cat(slip, "\n")  # Print each payment slip
}


