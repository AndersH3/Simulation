program iq_percent_difference
  implicit none
  integer, parameter :: n = 1000000
  real :: mean, stddev, rho
  real, allocatable :: x(:), y(:), percent_diff(:)
  real :: avg_percent_diff
  integer :: i

  call random_seed()

  ! Parameters for the simulation
  mean = 100.0
  stddev = 15.0
  rho = 0.8  ! Correlation between x and y (if simulated with correlation)

  allocate(x(n), y(n), percent_diff(n))

  ! Generate correlated IQ scores (Cholesky approach)
  do i = 1, n
     call random_number(x(i))
     call random_number(y(i))
     x(i) = mean + stddev * sqrt(-2.0*log(x(i))) * cos(2.0*3.1415927*y(i))
     call random_number(y(i))
     y(i) = mean + stddev * (rho * (x(i) - mean)/stddev + sqrt(1.0 - rho**2) * sqrt(-2.0*log(y(i))) * cos(2.0*3.1415927*y(i)))
  end do

  ! Compute percent differences
  do i = 1, n
     percent_diff(i) = 100.0 * abs(x(i) - y(i)) / ((x(i) + y(i)) / 2.0)
  end do

  ! Compute average percent difference
  avg_percent_diff = sum(percent_diff) / n

  print *, 'Average percent difference:', avg_percent_diff

  deallocate(x, y, percent_diff)
end program iq_percent_difference
