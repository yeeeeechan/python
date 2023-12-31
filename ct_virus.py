# def 구현하기

# 1. 리스트를 활용해 dfs 구현하기
# def dfs(graph, start_node):
#   # 기본적으로 항상 두 개의 리스트를 별도로 관리해 줘야 함.(방문이 필요한 노드, 이미 방문한 노드)
#   need_visited, visited = list(), list()
#   # 시작 노드 지정하기(방문해야 하는 노드에 시작 노드 넣기)
#   need_visited.append(start_node)
#   # 만약 아직도 방문이 필요한 노드가 있다면
#   while need_visited:
#     # 그중 가장 마지막 데이터를 추출(스택)
#     node = need_visited.pop()
#     # 만약 그 노드가 방문한 목록에 없다면
#     if node not in visited:
#       # 방문한 목록에 추가한다.
#       visited.apped(node)
#       # 인접 노드들은 방문 예정 리스트에 추가한다.
#       need_visited.extend(graph[node]) # extend는 리스트의 끝에 가장 바깥쪽 iterable(반복 가능한 객체)을 넣음
#   return visited

# # 2. deque를 활용한 구현
# def dfs2(graph, start_node) :
#   # deque 패키지 불러오기
#   frov collections ivport deque
#   visited = []
#   need_visited = deque()

#   # 시작 노드 설정
#   need_visited.append(start_node)

#   # 방문이 필요한 리스트가 아직 있다면
#   while need_visited:
#     # 그중 가장 마지막 데이터를 추출
#     node = need_visited.pop()
    
#     # 만약 그 노드가 방문한 리스트에 없다면
#     if node not in visited:
#       # 방문 리스트에 노드를 추가
#       visited.append(node)
#       # 인접 노드들을 방문 예정 리스트에 추가
#       need_visited.extend(graph[node])
#   return visited


  # 2606. 바이러스 (dfs_재귀함수 풀이)
n = int(input()) # 컴퓨터의 수 입력받기(정점의 수)
v = int(input()) # 컴퓨터 사이에 연결된 선의 개수(가장자리 수)

graph = [[] for i in range(n+1)] # (n+1)만큼 빈 2차원 리스트를 생성(인접 행렬), n+1을 하는 이유는 n번 컴퓨터를 n번 인덱스로 쓰기 위해
visited = [0]*(n+1) # (n+1) 길이의 0으로 이루어진 리스트 (0: 미방문, 1: 방문)

for i in range(v): # 그래프 생성, 연결선의 개수만큼 for문을 반복해 연결된 컴퓨터 번호를 각각 a, b로 입력받기
  a, b = map(int, input().split())
  graph[a] += [b] # a에 b를 연결
  graph[b] += [a] # b에 a를 연결 (쌍방 연결 / 1번에 2번이 연결되어 있고, 2번에 1번이 연결되어 있음을 나타내기 위함)

  # a, b를 입력받을 때 input() 대신 sys.stdin.readline()으로 입력을 받는 코드도 있는데,
  # 여러 줄의 문자열을 반복문으로 입력받을 때는 sys.stdin.readline()이 좀 더 빠르게 입력을 받을 수 있다고 합니다.
  
  # 쌍방 연결은 아래와 같이 .append()로도 동일한 처리가 가능
  # graph[a].append(b)
  # graph[b].append(a)

# (참고) 입력을 모두 마친 그래프 결과는 아래와 같다.
# 관련 개념: '인접 리스트'
graph[1] = [2, 5] # 1번 컴퓨터는 2번, 5번 컴퓨터와 연결되어 있음
graph[2] = [1, 3, 5] # 2번 컴퓨터는 1, 3, 5번 컴퓨터와 연결되어 있음
graph[3] = [2]
graph[4] = [7]
graph[5] = [1, 2, 6]
graph[6] = [5]
graph[7] = [4]


def dfs(m):
  visited[m] = 1 # 방문할 컴퓨터 번호를 m으로 입력받고, 방문 표시를 한다.
  for i in graph[m]: # graph[m]는 m번 컴퓨터에 연결된 컴퓨터들의 리스트
    if visited[i] == 0: # 각 컴퓨터를 i로 반복해 방문 여부를 검사하고, 만약 방문되지 않았다면(== 0)
      dfs(i) # 재귀 호출을 통해 해당 컴퓨터를 방문한다. 이 과정을 반복

dfs(1)
print(sum(visited)-1) # 1번 컴퓨터를 제외하고 1번 컴퓨터와 연결된 컴퓨터 개수를 출력해야 하므로 -1 함
# 파이썬에서 list는 함수 밖에서 선언된 뒤, 함수 안에서 변경되면 그 변경 사항이 함수 밖에도 동일하게 적용된다.


# BFS로 풀이 (deque 사용)
from collections import deque

visited[1] = 1 # 시작 컴퓨터 1을 방문으로 표시
Q = deque([1]) # 큐에 시작점 1을 넣고 초기화
while Q: # 큐에 노드가 남아 있는 동안 반복
  c = Q.popleft() # c=현재 컴퓨터, 왼쪽에서 요소를 꺼냄
  for nx in graph[c]:
    if visited[nx] == 0:
      Q.append(nx) # 오른쪽에 요소 추가
      visited[nx] = 1
print(sum(visited)-1)

