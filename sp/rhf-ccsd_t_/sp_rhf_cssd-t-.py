echo

start sp-rhf-ccsd_t_

memory 600 mb
geometry
O     0.000000000000    0.000000000000   -0.065638538099
H     0.000000000000   -0.757480611647    0.520865616174
H     0.000000000000    0.757480611647    0.520865616174
end

basis spherical
* library cc-pvdz
end

scf
 rhf
 thresh 1.0e-1
end

tce
 scf
 ccsd(t)
 thresh 1.0e-12
end

task tce energy