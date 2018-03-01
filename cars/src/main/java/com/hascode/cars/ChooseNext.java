package com.hascode.cars;

import java.util.ArrayList;

class ChooseNext {
    // maxiter massimo, lowerbound massimo e slack nullo per la soluzione più stretta possibile
    public static Integer chooseNext(ArrayList<Ride> r, Car c, Integer time, Integer maxIter, Integer lowerBound, Integer slack) {
        if (r.size() < 1) return -1;

        Integer out = 0, 
            max = getScore(r.get(0), time, c), 
            max_temp;
        
        for (Integer i = 1; i < r.size() && i < maxIter; i++){
            if (checkValidity(r.get(i), time, c, slack)) {
                max_temp = getScore(r.get(i), time, c);
                if (max_temp > max) {
                    out = i;
                    max = max_temp;
                    if (max >= lowerBound) {
                        c.x = r.get(out).x;
                        c.y = r.get(out).y;
                        return r.get(out).index;
                    }
                }
            }
        }
        c.x = r.get(out).x;
        c.y = r.get(out).y;
        return r.get(out).index;

    } // chooseNext

    public static boolean checkValidity(Ride r, Integer time, Car c, Integer slack) {
        // distanza inizio fine
        Integer distPercorso = Math.abs(r.x-r.a)+Math.abs(r.y-r.b),
            distCarRide = Math.abs(c.x-r.x)+Math.abs(c.y-r.y);

        // controllo che la car possa arrivare in tempo al Ride AND
        // controllo che la macchina arrivi antro s unita dalla partenza
        return (r.f <= time + distCarRide + distPercorso &&
            r.s >= time + distCarRide + slack);

    }

    public static Integer getScore(Ride r, Integer time, Car c) {
        Integer distPercorso = Math.abs(r.x-r.a)+Math.abs(r.y-r.b),
            bonus = 0;
        return distPercorso + bonus;
    }

}