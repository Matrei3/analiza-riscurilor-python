def construieste_graf():
	return {
		"Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
		"Zerind": {"Arad": 75, "Oradea": 71},
		"Oradea": {"Zerind": 71, "Sibiu": 151},
		"Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
		"Timisoara": {"Arad": 118, "Lugoj": 111},
		"Lugoj": {"Timisoara": 111, "Mehadia": 70},
		"Mehadia": {"Lugoj": 70, "Drobeta": 75},
		"Drobeta": {"Mehadia": 75, "Craiova": 120},
		"Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
		"Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
		"Fagaras": {"Sibiu": 99, "Bucharest": 211},
		"Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101},
		"Bucharest": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
		"Giurgiu": {"Bucharest": 90},
		"Urziceni": {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142},
		"Hirsova": {"Urziceni": 98, "Eforie": 86},
		"Eforie": {"Hirsova": 86},
		"Vaslui": {"Urziceni": 142, "Iasi": 92},
		"Iasi": {"Vaslui": 92, "Neamt": 87},
		"Neamt": {"Iasi": 87},
	}


def lista_adiacenta(graf):
	rezultat = {}
	for oras in graf:
		vecini = []
		for vecin in graf[oras]:
			vecini.append((vecin, graf[oras][vecin]))
		rezultat[oras] = vecini
	return rezultat


def matrice_costuri(graf):
	orase = sorted(graf.keys())
	index = {}
	i = 0
	while i < len(orase):
		index[orase[i]] = i
		i += 1

	n = len(orase)
	matrice = []
	i = 0
	while i < n:
		linie = []
		j = 0
		while j < n:
			if i == j:
				linie.append(0)
			else:
				linie.append(None)
			j += 1
		matrice.append(linie)
		i += 1

	for oras in graf:
		i = index[oras]
		for vecin in graf[oras]:
			j = index[vecin]
			matrice[i][j] = graf[oras][vecin]

	return orase, matrice


def muchii_si_numar(graf):
	muchii = []
	vazute = set()
	for oras in graf:
		for vecin in graf[oras]:
			pereche = tuple(sorted((oras, vecin)))
			if pereche not in vazute:
				vazute.add(pereche)
				muchii.append((pereche[0], pereche[1], graf[oras][vecin]))
	return len(muchii), muchii


def oras_cu_grad_maxim(graf):
	max_oras = None
	max_grad = -1
	for oras in graf:
		grad = len(graf[oras])
		if grad > max_grad:
			max_grad = grad
			max_oras = oras
	return max_oras, max_grad


def este_regulat(graf):
	grade = []
	for oras in graf:
		grade.append(len(graf[oras]))

	if len(grade) == 0:
		return True

	primul = grade[0]
	for grad in grade:
		if grad != primul:
			return False
	return True


def noduri_izolate(graf):
	izolate = []
	for oras in graf:
		if len(graf[oras]) == 0:
			izolate.append(oras)
	return izolate


def vecini_oras(graf, oras):
	if oras not in graf:
		return []

	rezultat = []
	for vecin in graf[oras]:
		rezultat.append((vecin, graf[oras][vecin]))
	return rezultat


def reconstruieste_drum(parinte, start, destinatie):
	if destinatie not in parinte and start != destinatie:
		return []

	drum = [destinatie]
	curent = destinatie
	while curent != start:
		curent = parinte[curent]
		drum.append(curent)

	drum.reverse()
	return drum


def dijkstra(graf, start, destinatie):
	if start not in graf or destinatie not in graf:
		return None, []

	dist = {}
	parinte = {}
	nevizitate = []
	inf = 10 ** 12

	for oras in graf:
		dist[oras] = inf
		nevizitate.append(oras)

	dist[start] = 0

	while len(nevizitate) > 0:
		# Gasim nodul nevizitat cu distanta minima (fara heap, doar cicluri).
		oras_min = None
		dist_min = inf
		for oras in nevizitate:
			if dist[oras] < dist_min:
				dist_min = dist[oras]
				oras_min = oras

		if oras_min is None:
			break

		nevizitate.remove(oras_min)

		if oras_min == destinatie:
			break

		for vecin in graf[oras_min]:
			cost = graf[oras_min][vecin]
			noua_dist = dist[oras_min] + cost
			if noua_dist < dist[vecin]:
				dist[vecin] = noua_dist
				parinte[vecin] = oras_min

	if dist[destinatie] >= inf:
		return None, []

	return dist[destinatie], reconstruieste_drum(parinte, start, destinatie)


def bfs_drum_minim_pasi(graf, start, destinatie):
	if start not in graf or destinatie not in graf:
		return []

	coada = [start]
	vizitat = {start}
	parinte = {}
	pozitie = 0

	while pozitie < len(coada):
		curent = coada[pozitie]
		pozitie += 1

		if curent == destinatie:
			break

		for vecin in graf[curent]:
			if vecin not in vizitat:
				vizitat.add(vecin)
				parinte[vecin] = curent
				coada.append(vecin)

	if destinatie not in vizitat:
		return []

	return reconstruieste_drum(parinte, start, destinatie)


def exista_drum_dfs_recursiv(graf, start, destinatie):
	if start not in graf or destinatie not in graf:
		return False

	vizitat = set()

	def dfs(nod):
		if nod == destinatie:
			return True
		vizitat.add(nod)
		for vecin in graf[nod]:
			if vecin not in vizitat:
				if dfs(vecin):
					return True
		return False

	return dfs(start)


def este_conex(graf):
	if len(graf) == 0:
		return True

	start = None
	for oras in graf:
		start = oras
		break

	vizitat = set()
	stiva = [start]

	while len(stiva) > 0:
		nod = stiva.pop()
		if nod in vizitat:
			continue
		vizitat.add(nod)
		for vecin in graf[nod]:
			if vecin not in vizitat:
				stiva.append(vecin)

	return len(vizitat) == len(graf)


def lanturi_cost_exact(graf, cost_tinta):
	rezultate = []
	canonice = set()

	def dfs(nod_curent, cost_curent, drum, vizitat):
		if cost_curent == cost_tinta and len(drum) >= 2:
			t = tuple(drum)
			r = tuple(reversed(drum))
			cheie = t if t < r else r
			if cheie not in canonice:
				canonice.add(cheie)
				rezultate.append(list(drum))
			return

		if cost_curent > cost_tinta:
			return

		for vecin in graf[nod_curent]:
			if vecin not in vizitat:
				cost = graf[nod_curent][vecin]
				vizitat.add(vecin)
				drum.append(vecin)
				dfs(vecin, cost_curent + cost, drum, vizitat)
				drum.pop()
				vizitat.remove(vecin)

	for start in graf:
		dfs(start, 0, [start], {start})

	return rezultate


def este_complet_si_muchii_lipsa(graf):
	orase = sorted(graf.keys())
	lipsa = []
	i = 0
	while i < len(orase):
		j = i + 1
		while j < len(orase):
			a = orase[i]
			b = orase[j]
			if b not in graf[a]:
				lipsa.append((a, b))
			j += 1
		i += 1

	return len(lipsa) == 0, lipsa


def muchii_cu_extremitati_aceeasi_paritate(graf):
	orase = sorted(graf.keys())
	index = {}
	i = 0
	while i < len(orase):
		index[orase[i]] = i + 1
		i += 1

	_, muchii = muchii_si_numar(graf)
	rezultat = []
	for a, b, cost in muchii:
		if index[a] % 2 == index[b] % 2:
			rezultat.append((a, b, cost))
	return rezultat


def tur_dfs_hamiltonian(graf, start):
	if start not in graf:
		return []

	n = len(graf)
	drum = [start]
	vizitat = {start}

	def backtracking(nod):
		if len(drum) == n:
			return True

		for vecin in graf[nod]:
			if vecin not in vizitat:
				vizitat.add(vecin)
				drum.append(vecin)
				if backtracking(vecin):
					return True
				drum.pop()
				vizitat.remove(vecin)
		return False

	if backtracking(start):
		return drum
	return []


def format_matrice_costuri(orase, matrice):
	linii = []
	antet = " " * 12
	for oras in orase:
		antet += f"{oras[:10]:>11} "
	linii.append(antet)

	i = 0
	while i < len(orase):
		rand = f"{orase[i][:10]:>11} "
		j = 0
		while j < len(orase):
			val = matrice[i][j]
			if val is None:
				txt = "-"
			else:
				txt = str(val)
			rand += f"{txt:>11} "
			j += 1
		linii.append(rand)
		i += 1

	return "\n".join(linii)


def main():
	graf = construieste_graf()

	print("1) Lista de adiacenta:")
	adj = lista_adiacenta(graf)
	for oras in sorted(adj.keys()):
		print(f"{oras}: {adj[oras]}")

	print("2) Matricea costurilor:")
	orase, mat = matrice_costuri(graf)
	print(format_matrice_costuri(orase, mat))

	nr_muchii, muchii = muchii_si_numar(graf)
	print("3) Numar muchii:", nr_muchii)
	print("Muchii:", muchii)

	oras_max, grad_max = oras_cu_grad_maxim(graf)
	print("4) Oras cu grad maxim:", oras_max, "(grad", grad_max, ")")

	print("5) Graful este regulat?", este_regulat(graf))

	print("6) Noduri izolate:", noduri_izolate(graf))

	oras_x = "Sibiu"
	print(f"7) Vecinii orasului {oras_x}:", vecini_oras(graf, oras_x))

	dist_ne, drum_ne = dijkstra(graf, "Neamt", "Eforie")
	print("8) Dijkstra Neamt -> Eforie:")
	print("Distanta:", dist_ne)
	print("Drum:", drum_ne)

	dist_ab, drum_ab = dijkstra(graf, "Arad", "Bucharest")
	print("9) Dijkstra Arad -> Bucharest:")
	print("Distanta:", dist_ab)
	print("Drum:", drum_ab)

	lanturi = lanturi_cost_exact(graf, 198)
	print("10) Lanturi cu cost total 198:")
	print(lanturi)

	complet, lipsa = este_complet_si_muchii_lipsa(graf)
	print("11) Graful este complet?", complet)
	if not complet:
		print("Muchii lipsa:", lipsa)

	print("12) Muchii cu extremitati de aceeasi paritate:")
	print(muchii_cu_extremitati_aceeasi_paritate(graf))

	drum_bfs = bfs_drum_minim_pasi(graf, "Arad", "Bucharest")
	print("13) BFS Arad -> Bucharest (minim pasi):")
	print("Drum:", drum_bfs)
	print("Numar pasi:", max(0, len(drum_bfs) - 1))

	a, b = "Arad", "Eforie"
	print(f"14) Exista drum intre {a} si {b}?", exista_drum_dfs_recursiv(graf, a, b))

	print("15) Graful este conex?", este_conex(graf))

	tur = tur_dfs_hamiltonian(graf, "Arad")
	print("16) Tur DFS (vizitare unica) pornind din Arad:")
	if len(tur) == 0:
		print("Nu exista un astfel de tur pentru acest graf.")
	else:
		print(tur)


if __name__ == "__main__":
	main()
