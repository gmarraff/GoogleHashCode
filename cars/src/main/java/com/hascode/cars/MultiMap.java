package com.hascode.cars	;

import java.util.List;
import java.util.Set;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.function.BiConsumer;



/**
 * This class implements a MultiMap data structure. A MultiMap is an associative structure where multiple elements can be mapped
 * under a one key. An an example consider the following sequence of statements:
 * 1. map.put(k1, v1);
 * 2. map.put(k1, v2);
 * 3. List<V> = map.get(k1);
 *
 * The last operation should return a List<V> of values comprised of the entries {v1, v2}
 */
public class MultiMap<K, V> {
	private HashMap <K, ArrayList<V>> map;

	/**
	 * Sole constructor of the class which builds an empty MultiMap.
	 */
	public MultiMap() {
		map = new HashMap<K, ArrayList<V>>();
	}

	/**
	 * Stores the value (value)given as an input under the key (key).
	 *
	 * @param key: 		key parameter which serves as an index in the MultiMap data structure
	 * @param value: 	value parameter to be index under the key
	 */
	public void put(K key, V value) {
		if(!map.containsKey(key)) map.put(key, new ArrayList<V>());
		map.get(key).add(value);
	}

	/**
	 * Returns a Set view of the keys contained in this map.
	 *
	 * @return a set view of the keys contained in this map.
	 */
	public Set<K> keySet() {
		return map.keySet();
	}

	/**
	 * Returns a List of objects stored under the key (key).
	 *
	 * @return a List of objects stored under the key.
	 */
	public List<V> get(Object key) {
		return map.get(key);
	}

	public void forEach(BiConsumer <? super K,? super List<V>> action){
		map.forEach(action);
	}
}
