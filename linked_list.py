class Node:
  '''
  Represents a node in a linked list
  contains two values - data and the pointer to the next node
  '''
  data = None
  nextNode = None

  def __init__(self, data) -> None:
    self.data = data
  
  def __repr__(self) -> str:
    return f'<Node data: {self.data}>'
  



class LinkedList:
  '''
  Represents a singly linked list
  '''

  def __init__(self) -> None:
    self.head = None

  def __repr__(self) -> str:
    '''
    Represents the string representation of the List
    O(n) time
    '''
    nodes = []
    current = self.head

    while current:
      if current is self.head:
        nodes.append(f'[head: {current.data}]')

      elif current.nextNode == None:
        nodes.append(f'[tail: {current.data}]')
      
      else:
        nodes.append(f'[{current.data}]')

      current = current.nextNode
    return ' -> '.join(nodes)
  
  def isEmpty(self) -> bool:
    '''
    Checks if list is empty and returns a boolean
    O(1) time
    '''
    return self.head == None
  
  def size(self) -> int:
    '''
    loops through the list to calculate its size
    O(n) time
    '''
    count = 0
    current = self.head

    while current:
      count += 1
      current = current.nextNode
    
    return count
  
  def prepend(self, data) -> None:
    '''
    Adds a new node to the head of the list
    O(1) time
    '''
    newNode = Node(data)
    newNode.nextNode = self.head
    self.head = newNode


  def search(self, key):
    '''
    Searches the linked list for the first node's data that matches the given key
    returns the node or 'None' if not found
    O(n) time
    '''

    current = self.head

    while current:
      if current.data == key:
        return current
      else:
        current = current.nextNode

    return None

  
  def insert(self, data, index: int) -> None:
    '''
    Inserts a new node containing the given data at a specified (zero based) index : starting at the head
    Throws an error if index is negative or out of range
    O(n) time
    '''

    if index < 0:
      raise IndexError('Index cannot be negative!')

    elif index == 0:
      # newNode = Node(data)
      # newNode.nextNode = self.head
      # self.head = newNode
      self.prepend(data)
    
    elif index > 0:
      current = self.head
      iterations = 1

      while current:
        if iterations == index:
          newNode = Node(data)
          newNode.nextNode = current.nextNode
          current.nextNode = newNode
          return None

        iterations += 1
        current = current.nextNode

      else:
        raise IndexError('Index is out of range!')

  
  def remove(self, key) -> Node:
    '''
    Removes a node that contains same data as the key provided by traversing the linked list
    Returns the deleted Node or raises an exception if a Node's data with the given key is not found
    O(n) time
    '''
    
    prev = None
    current = self.head

    # traverse the list and compare Node's data to key
    while current:
      if current.data == key:
        prev.nextNode = current.nextNode
        return current

      prev = current
      current = current.nextNode

    # raise an exception if loop ends and key is not found
    else:
      raise Exception('Node containing given data not found!')
  

  def removeByIndex(self, index: int) -> Node:
    '''
    Removes a node at a specified (zero based) index : starting at the head
    Returns the removed Node or raises an exception if index is negative or out of range
    O(n) time
    '''

    prev = None
    current = self.head
    position = 0

    if index < 0:
      raise IndexError('Index cannot be negative!')
    
    elif index == 0:
      self.head = current.nextNode
      return current

    while current:
      if position == index:
        prev.nextNode = current.nextNode
        return current

      prev = current
      current = current.nextNode
      position += 1
      pass

    else:
      raise IndexError('Index out of range!')
