% Rules as per the frame represtation of the knowledge.
rel(opal, isa, car).
rel(pontiac_grand_prix, isa, car).
rel(flx_drive, isa, train).
rel(silver_bullet, isa, car).
rel(f150_lightning, isa, car).
rel(peral, isa, aquatic_vehicles).
rel(qe2, isa, aquatic_vehicles).
rel(multnohma, isa, aquatic_vehicles).
rel(airforce_one, isa, airplane).
rel(train, subset, land_vehicles).
rel(car, subset, land_vehicles).
rel(airplane, subset, aricraft_vehicles).
rel(land_vehicles, subset, vehicle).
rel(aquatic_vehicles, subset, vehicle).
rel(aricraft_vehicles, subset, vehicle).
property(wheels, flx_drive, 8).
property(fuel, f150_lightning, electric).
property(fuel, peral, electric).
property(wheels, multnohma, 1).
property(wheels, land_vehicles, 4).
property(fuel, land_vehicles, gasoline).
property(wheels, aquatic_vehicles, 0).
property(fuel, aquatic_vehicles, gasoline).
property(wheels, aircraft_vehicles, 3).
property(fuel, aircraft_vehicles, gasoline).
property(fuel, vehicle, gasoline).

% functions to query property like wheels or fuel of a given entity.
property(P, X, Y) :-  rel(X, isa, Z),
                      property(P, Z, Y).

property(P, X, Y) :-  rel(X, subset, Z),
                      property(P, Z, Y).

% functions to query type of a given entity.
type(X,Y):- rel(X, subset, Y).
type(X,Y):- rel(X, subset, Z),
            type(Z,Y).

type(X,Y):- rel(X, isa, Y).
type(X,Y):- rel(X, isa, Z),
            type(Z,Y).
