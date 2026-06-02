def modul_numar(n):
	return abs(n)


def lungime_lista(lista):
	return len(lista)


def lista_cifre(n):
	x = modul_numar(n)
	if x == 0:
		return [0]

	invers = []
	while x > 0:
		invers.append(x % 10)
		x //= 10

	cifre = []
	i = lungime_lista(invers) - 1
	while i >= 0:
		cifre.append(invers[i])
		i -= 1

	return cifre


def numar_din_cifre(cifre):
	nr = 0
	for cifra in cifre:
		nr = nr * 10 + cifra
	return nr


def exista_in_lista(lista, valoare):
	return valoare in lista


def numar_cifre(n):
	x = modul_numar(n)
	if x == 0:
		return 1

	cnt = 0
	while x > 0:
		cnt += 1
		x //= 10
	return cnt


def oglindit_numar(n):
	semn = 1
	if n < 0:
		semn = -1

	x = modul_numar(n)
	ogl = 0
	while x > 0:
		ogl = ogl * 10 + (x % 10)
		x //= 10
	return semn * ogl


def mesaj_semn(n):
	if n > 0:
		return "Pozitiv."
	if n < 0:
		return "Negativ."
	return "Zero."


def numere_prin_eliminare_o_cifra(n):
	cifre = lista_cifre(n)
	k = lungime_lista(cifre)
	semn = 1
	if n < 0:
		semn = -1

	rezultate = []

	i = 0
	while i < k:
		cifre_noi = []
		j = 0
		while j < k:
			if j != i:
				cifre_noi.append(cifre[j])
			j += 1

		if lungime_lista(cifre_noi) == 0:
			valoare = 0
		else:
			valoare = numar_din_cifre(cifre_noi)

		rezultate.append(semn * valoare)
		i += 1

	return rezultate


def suma_cifrelor(n):
	x = modul_numar(n)
	suma = 0

	if x == 0:
		return 0

	while x > 0:
		suma += x % 10
		x //= 10
	return suma


def produs_cifrelor(n):
	x = modul_numar(n)
	if x == 0:
		return 0

	produs = 1
	while x > 0:
		produs *= x % 10
		x //= 10
	return produs


def este_palindrom(n):
	return modul_numar(n) == modul_numar(oglindit_numar(n))


def este_numar_perfect(n):
	if n <= 1:
		return False

	suma_divizori = 0
	d = 1
	while d < n:
		if n % d == 0:
			suma_divizori += d
		d += 1

	return suma_divizori == n


def cifre_sortate_crescator_descrescator(n):
	cifre = lista_cifre(n)
	asc = []
	for c in cifre:
		asc.append(c)

	k = lungime_lista(asc)
	i = 0
	while i < k - 1:
		j = 0
		while j < k - i - 1:
			if asc[j] > asc[j + 1]:
				asc[j], asc[j + 1] = asc[j + 1], asc[j]
			j += 1
		i += 1

	desc = []
	i = k - 1
	while i >= 0:
		desc.append(asc[i])
		i -= 1

	return asc, desc


def cifre_catre_text(cifre):
	text = ""
	for cifra in cifre:
		text += str(cifra)
	return text


def permutari_cifre(n):
	cifre = lista_cifre(n)
	k = lungime_lista(cifre)

	if k > 5:
		return []

	semn = 1
	if n < 0:
		semn = -1

	folosit = []
	i = 0
	while i < k:
		folosit.append(0)
		i += 1

	curent = []
	rezultate = []

	def backtracking():
		if lungime_lista(curent) == k:
			valoare = numar_din_cifre(curent)
			valoare *= semn
			if not exista_in_lista(rezultate, valoare):
				rezultate.append(valoare)
			return

		idx = 0
		while idx < k:
			if folosit[idx] == 0:
				folosit[idx] = 1
				curent.append(cifre[idx])
				backtracking()
				curent.pop()
				folosit[idx] = 0
			idx += 1

	backtracking()
	return rezultate


def citeste_numar_intreg():
	while True:
		try:
			return int(input("n: "))
		except ValueError:
			print("Invalid")


def main():
	n = citeste_numar_intreg()

	print("1) Numarul de cifre:")
	print(numar_cifre(n))

	print("2) Oglinditul numarului:")
	print(oglindit_numar(n))

	print("3) Semnul numarului:")
	print(mesaj_semn(n))

	print("4) Numere obtinute prin eliminarea unei singure cifre:")
	print(numere_prin_eliminare_o_cifra(n))

	print("5) Suma cifrelor:")
	print(suma_cifrelor(n))

	print("6) Produsul cifrelor:")
	print(produs_cifrelor(n))

	print("7) Verificare palindrom:")
	if este_palindrom(n):
		print("Numarul este palindrom.")
	else:
		print("Numarul NU este palindrom.")

	print("8) Verificare numar perfect:")
	if este_numar_perfect(n):
		print("Numarul este perfect.")
	else:
		print("Numarul NU este perfect.")

	print("9) Cifre in ordine crescatoare si descrescatoare:")
	cifre_asc, cifre_desc = cifre_sortate_crescator_descrescator(n)
	print("Crescator:", cifre_catre_text(cifre_asc))
	print("Descrescator:", cifre_catre_text(cifre_desc))

	print("10) Permutari ale cifrelor (maxim 5 cifre):")
	perm = permutari_cifre(n)
	if lungime_lista(perm) == 0 and numar_cifre(n) > 5:
		print("Numarul are mai mult de 5 cifre. Permutarile nu sunt generate.")
	else:
		print(perm)


if __name__ == "__main__":
	main()
