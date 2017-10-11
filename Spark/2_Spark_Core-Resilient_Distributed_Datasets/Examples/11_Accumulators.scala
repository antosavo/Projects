//An accumulator is an add-only variable that can be updated 
//by tasks running on different nodes and read by the driver program.

case class Customer(id: Long, name: String)

val customers = sc.parallelize(List(
                Customer(1, "Tom"),
                Customer(2, "Harry"),
                Customer(-1, "Paul")))

val badIds = sc.accumulator(0, "Bad id accumulator")

val validCustomers = customers.filter(c => if (c.id < 0) {
                                        badIds += 1
                                        false
                                        } else true
                                        )

val validCustomerIds = validCustomers.count
val invalidCustomerIds = badIds.value