package com.hascode.cars;

import java.util.List;

class ChooseNext {
    // maxiter massimo, lowerbound massimo e slack nullo per la soluzione più stretta possibile
    public static Integer chooseNext(
        List<Ride> r, // array di Rider
        Car c, // macchina in questione
        Integer time, // tempo corrente
        Integer maxTime, // tempo massimo totale
        Integer maxIter, // numero massimo di iterazioni possibili
        Integer lowerBound, // score minimo richiesto per uscire prima
        Integer slack, // quanto prima fare arrivare la macchina rispetto allo start time
        Integer bonus // bonus per arrivare in tempo
        ) {
        if (r.size() < 1) return -1; // casi base non ho elementi in r

        Integer out = 0, // indice (interno a r) dell'elemento scelto
            max = getScore(r.get(0), c, time, bonus), // score massima
            max_temp; // score temporanea all'interno del ciclo
        
        for (Integer i = 1; i < r.size() && i < maxIter; i++){
            // controllo validità del rider r con la macchina c all'istante time con uno slack iniziale
            if (checkValidity(r.get(i), time, maxTime, c, slack)) {
                max_temp = getScore(r.get(i), c, time, bonus);
                // controllo se miglioro la soluzione migliore
                if (max_temp > max) {
                    out = i;
                    max = max_temp;
                    // controllo se supero l'upper bound
                    if (max >= lowerBound) {
                        // modifico la posizione della macchina prima di ritornare
                        c.x = r.get(out).x;
                        c.y = r.get(out).y;
                        r.get(out).f = 0; // per non riprenderla mai più la stessa macchina
                        return r.get(out).index;
                    }
                }
            }
        }
        // modifico la posizione della macchina prima di ritornare
        c.x = r.get(out).x;
        c.y = r.get(out).y;
        r.get(out).f = 0; // per non riprenderla mai più la stessa macchina
        return r.get(out).index;

    } // chooseNext

    public static boolean checkValidity(Ride r, Integer time, Integer maxTime, Car c, Integer slack) {
        // distanza inizio fine
        Integer distPercorso = Math.abs(r.x-r.a)+Math.abs(r.y-r.b),
            distCarRide = Math.abs(c.x-r.x)+Math.abs(c.y-r.y);

        // controllo che la car possa arrivare in tempo al Ride AND
        // controllo che la macchina arrivi antro s unita dalla partenza
        return (time + distCarRide + distPercorso <= maxTime &&
            time + distCarRide + distPercorso <= r.f &&
            time + distCarRide + slack >= r.s);

    }

    public static Integer getScore(Ride r, Car c, Integer time, Integer bonus) {
        Integer distPercorso = Math.abs(r.x-r.a)+Math.abs(r.y-r.b),
            b = 0;
        if (r.s == time) b = bonus;
        return distPercorso + b;
    }

}