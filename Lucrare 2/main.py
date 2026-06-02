def citeste_int(mesaj):
	while True:
		try:
			return int(input(mesaj))
		except ValueError:
			print("Valoare invalida. Introdu un numar intreg.")


def citeste_vector():
	n = citeste_int("Numarul de elemente din vector: ")
	vector = []
	for i in range(n):
		x = citeste_int(f"v[{i}] = ")
		vector.append(x)
	return vector


def minim_maxim_si_pozitii(vector):
	if not vector:
		return None

	minim = min(vector)
	maxim = max(vector)
	pozitii_minim = [i for i, valoare in enumerate(vector) if valoare == minim]
	pozitii_maxim = [i for i, valoare in enumerate(vector) if valoare == maxim]

	return minim, maxim, pozitii_minim, pozitii_maxim


def elimina_duplicate(vector):
	vazute = set()
	rezultat = []
	for element in vector:
		if element not in vazute:
			rezultat.append(element)
			vazute.add(element)
	return rezultat


def este_palindrom(vector):
	return vector == vector[::-1]


def citeste_matrice_tastatura():
	n = citeste_int("n: ")
	m = citeste_int("m: ")

	matrice = []
	for i in range(n):
		linie = []
		for j in range(m):
			element = citeste_int(f"a[{i}][{j}] = ")
			linie.append(element)
		matrice.append(linie)
	return matrice


def matrice_transpusa(matrice):
	if not matrice:
		return []
	return [list(coloana) for coloana in zip(*matrice)]


def este_patratica(matrice):
	return bool(matrice) and all(len(linie) == len(matrice) for linie in matrice)


def este_simetrica(matrice):
	if not este_patratica(matrice):
		return False

	n = len(matrice)
	for i in range(n):
		for j in range(i + 1, n):
			if matrice[i][j] != matrice[j][i]:
				return False
	return True


def diagonale(matrice):
	if not este_patratica(matrice):
		return None, None

	n = len(matrice)
	diagonala_principala = [matrice[i][i] for i in range(n)]
	diagonala_secundara = [matrice[i][n - 1 - i] for i in range(n)]
	return diagonala_principala, diagonala_secundara


def linie_sau_coloana_cu_suma_maxima(matrice):
	if not matrice or not matrice[0]:
		return None

	sume_linii = [sum(linie) for linie in matrice]
	sume_coloane = [sum(col) for col in zip(*matrice)]

	index_linie_max = max(range(len(sume_linii)), key=lambda i: sume_linii[i])
	index_coloana_max = max(range(len(sume_coloane)), key=lambda j: sume_coloane[j])

	suma_linie_max = sume_linii[index_linie_max]
	suma_coloana_max = sume_coloane[index_coloana_max]

	if suma_linie_max >= suma_coloana_max:
		tip = "linie"
		index = index_linie_max
		suma = suma_linie_max
	else:
		tip = "coloana"
		index = index_coloana_max
		suma = suma_coloana_max

	return {
		"tip": tip,
		"index": index,
		"suma": suma,
		"sume_linii": sume_linii,
		"sume_coloane": sume_coloane,
	}


def afiseaza_matrice(matrice):
	for linie in matrice:
		print(" ".join(str(x) for x in linie))


def alege_matrice():
	print("Alegere introducere matrice:")
	print("1 - Tastatura")
	print("2 - Manual in cod")

	optiune = citeste_int("")

	if optiune == 1:
		return citeste_matrice_tastatura()

	return [
		[1, 2, 3],
		[2, 5, 6],
		[3, 6, 9],
	]


def main():
	vector = citeste_vector()

	rezultat_min_max = minim_maxim_si_pozitii(vector)
	if rezultat_min_max is not None:
		minim, maxim, pozitii_minim, pozitii_maxim = rezultat_min_max
		print(f"Minim = {minim}, pozitii = {pozitii_minim}")
		print(f"Maxim = {maxim}, pozitii = {pozitii_maxim}")

	vector_fara_duplicate = elimina_duplicate(vector)
	print(f"Set: {vector_fara_duplicate}")

	vector_crescator = sorted(vector)
	vector_descrescator = sorted(vector, reverse=True)
	print(f"Crescator: {vector_crescator}")
	print(f"Descrescator: {vector_descrescator}")

	if este_palindrom(vector):
		print("Palindrom")
	else:
		print("!Palindrom")

	matrice = alege_matrice()
	afiseaza_matrice(matrice)

	transpusa = matrice_transpusa(matrice)
	print("Transpusa matricei:")
	afiseaza_matrice(transpusa)

	if este_patratica(matrice):
		print("Matricea este patratica.")
		if este_simetrica(matrice):
			print("Simetrica")
		else:
			print("!Simetrica")

		diagonala_principala, diagonala_secundara = diagonale(matrice)
		print(f"Diagonala principala: {diagonala_principala}")
		print(f"Diagonala secundara: {diagonala_secundara}")
	else:
		print("!Patratica")

	rezultat_sume = linie_sau_coloana_cu_suma_maxima(matrice)
	if rezultat_sume is not None:
		print(f"Sum linii: {rezultat_sume['sume_linii']}")
		print(f"Sum coloane: {rezultat_sume['sume_coloane']}")
		print(
			f"{rezultat_sume['tip'].capitalize()}a cu suma maxima este {rezultat_sume['tip']} "
			f"cu index {rezultat_sume['index']} si suma {rezultat_sume['suma']}."
		)


if __name__ == "__main__":
	main()
