program iq_simulation
  use iso_fortran_env, only: real64
  implicit none
  !--------------------------------------------------------------------
  ! This program simulates IQ test–retest percent-differences and
  ! inter-individual percent variability in IQ scores for a large sample.
  ! It models two sequential IQ test scores per person as correlated
  ! normal variables (ρ = 0.6), then computes and prints the average
  ! percent difference within individuals (intra-individual) and between
  ! randomly paired individuals (inter-individual). Parallel reductions
  ! use OpenMP for the heavy loops.
  !--------------------------------------------------------------------

  integer, parameter    :: N = 10000000, M = 10000000
  real(real64), parameter :: mu    = 100.0_real64
  real(real64), parameter :: sigma =  15.0_real64
  real(real64), parameter :: rho   =   0.6_real64

  real(real64), allocatable :: score1(:), score2(:)
  real(real64) :: intra_sum, inter_sum
  integer :: i, j, idx1, idx2
  real(real64) :: u1, u2, z1, z2

  ! Initialize the intrinsic RNG with a distinct seed
  call random_seed()

  ! Allocate arrays to hold generated scores
  allocate(score1(N), score2(N))

  !--------------------------------------------------------------------
  ! Generate correlated IQ scores serially
  !--------------------------------------------------------------------
  do i = 1, N
    call random_number(u1)
    call random_number(u2)
    if (u1 <= 0.0_real64) u1 = 1.0e-10_real64
    z1 = sqrt(-2.0_real64 * log(u1)) * cos(2.0_real64 * acos(-1.0_real64) * u2)
    z2 = sqrt(-2.0_real64 * log(u1)) * sin(2.0_real64 * acos(-1.0_real64) * u2)
    score1(i) = mu + sigma * z1
    score2(i) = mu + sigma * (rho * z1 + sqrt(1.0_real64 - rho*rho) * z2)
  end do

  !--------------------------------------------------------------------
  ! Compute average intra-individual percent difference in parallel
  !--------------------------------------------------------------------
  intra_sum = 0.0_real64
  !$omp parallel do default(shared) private(i) reduction(+:intra_sum)
  do i = 1, N
    intra_sum = intra_sum + 100.0_real64 * abs(score1(i) - score2(i)) / ((score1(i) + score2(i)) / 2.0_real64)
  end do
  !$omp end parallel do

  print *, "Average intra-individual percent difference =", intra_sum / real(N, real64)

  !--------------------------------------------------------------------
  ! Compute average inter-individual percent difference in parallel
  !--------------------------------------------------------------------
  inter_sum = 0.0_real64
  !$omp parallel do default(shared) private(j, idx1, idx2, u1, u2) reduction(+:inter_sum)
  do j = 1, M
    do
      call random_number(u1)
      idx1 = int(u1 * N) + 1
      call random_number(u2)
      idx2 = int(u2 * N) + 1
      if (idx1 /= idx2) exit
    end do
    inter_sum = inter_sum + 100.0_real64 * abs(score1(idx1) - score1(idx2)) / ((score1(idx1) + score1(idx2)) / 2.0_real64)
  end do
  !$omp end parallel do

  print *, "Average inter-individual percent difference =", inter_sum / real(M, real64)

  ! Clean up
  deallocate(score1, score2)
end program iq_simulation
