import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

/**
 * Class to create a planning graph and extract a plan from it.
 */
public class GraphPlan {

	// Boolean to check if a solution is found.
	static boolean solutionFound = false;
	
	// Variables to persist set of states and actions.
	static HashSet<String> initialState = new HashSet<>();
	static HashSet<String> goalState = new HashSet<>();
	static HashSet<Action> actions = new HashSet<>();
	
	// Action and state nodes.
	static ArrayList<HashMap<String, ActionNode>> actionNodes = new ArrayList<>();
	static ArrayList<HashMap<String, StateNode>> stateNodes = new ArrayList<>();
	
	// Variables to store all the mutexes related information.
	static ArrayList<HashSet<String>> statesMutex = new ArrayList<>();
	static ArrayList<HashSet<String>> actionsMutex = new ArrayList<>();
	
	// Variable to keep track of the actions in the solution.
	static ArrayList<HashSet<String>> actionTrace = new ArrayList<>();

	// Variables to keep track of mutexes.
	static HashSet<String> cnMutex = new HashSet<>();
	static HashSet<String> ieMutex = new HashSet<>();
	static HashSet<String> iMutex =  new HashSet<>();
	static HashSet<String> nlMutex = new HashSet<>();
	static HashSet<String> isMutex = new HashSet<>();

	/**
	 * Method to trim all the array elements with spaces.
	 *
	 * @param initialArray: array elements to be trimmed
	 */
	static void trimArrayElements(String[] initialArray){
		for (int index = 0; index < initialArray.length; index++)
			initialArray[index] = initialArray[index].trim();
	}

	/**
	 * Method to extract the elements of initial and goal states.
	 *
	 * @param line: line to split
	 * @return returns the list of elements
	 */
	static String[] extractBoundaryStateElements(String line){
		return (line.substring(5)).trim().split(",");
	}

	/**
	 * Method to parse the input file in PDDL format.
	 *
	 * @param inputFile: input file
	 */
	static void parseInput(String inputFile) {
		try {
			String eachLine;
			String actionName = "";
			String[] preConditions = {};
			String[] postEffects = {};
			FileReader fileReader = new FileReader(inputFile);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			while((eachLine = bufferedReader.readLine()) != null) {
				if(eachLine.trim().length() == 0){
					continue;
				}
				switch (eachLine.charAt(0)) {
					case 'I': {
						String[] initString = extractBoundaryStateElements(eachLine);
						trimArrayElements(initString);
						Collections.addAll(initialState, initString);
						break;
					}
					case 'G': {
						String[] goalString = extractBoundaryStateElements(eachLine);
						trimArrayElements(goalString);
						Collections.addAll(goalState, goalString);
						break;
					}
					case 'A': {
						if (!actionName.equals("")) {
							actions.add(new Action(actionName, preConditions, postEffects));
						}
						actionName = eachLine.substring(7).trim();
						break;
					}
					case 'P': {
						preConditions = (eachLine.substring(8)).trim().split(",");
						trimArrayElements(preConditions);
						break;
					}
					case 'E': {
						postEffects = (eachLine.substring(7)).trim().split(",");
						trimArrayElements(postEffects);
						break;
					}
				}
            }
			if (!actionName.equals("")) {
				actions.add(new Action(actionName, preConditions, postEffects));
			}
			bufferedReader.close();
		} catch(IOException exception) {
			System.out.println("Error parsing the input file");
			exception.printStackTrace();
        }
	}

	/**
	 * Method to make initial state of the planning graph.
	 */
	public static void makeInitialState() {
		for (String predicate: goalState) {
			if(predicate.charAt(0) == '-'){
				initialState.add(predicate.substring(1));
			}
			else{
				initialState.add('-' + predicate);
			}
		}
		HashMap<String, StateNode> initStateNodes = new HashMap<>();
		for (String initState: initialState) {
			initStateNodes.put(initState, new StateNode(initState));
		}
		stateNodes.add(initStateNodes);
		statesMutex.add(new HashSet<>());
	}

	/**
	 * Prints mutexes in each layer.
	 *
	 * @param mutexList: list of mutexes
	 * @param mutexName: Type of mutex
	 */
	public static void logMutexes(HashSet<String> mutexList, String mutexName) {
		if(mutexList.isEmpty()){
			return;
		}
		ArrayList<String> mutexes = new ArrayList<>();
		System.out.print("Mutex Type " + mutexName + " Found:");
		for (String m: mutexList) {
			mutexes.add("(" + m + ")");
		}
		System.out.println(mutexes);
		System.out.println();
	}

	/**
	 * Prints actions at each layer.
	 *
	 * @param actions: list of actions
	 */
	public static void logActions(HashMap<String, ActionNode> actions) {
		if(actions.isEmpty()){
			return;
		}
		System.out.println("Adding Actions: ");
		System.out.println(actions.keySet());
	}

	/**
	 * Prints states at each layer.
	 *
	 * @param states: list of states
	 */
	public static void logStates(HashMap<String, StateNode> states) {
		if(states.isEmpty()){
			return;
		}
		System.out.println("Next States: ");
		System.out.println(states.keySet());
	}

	/**
	 * Prints out the plan extract.
	 *
	 * @param actions list of actions in each layer.
	 */
	public static void logPlanExtract(ArrayList<HashSet<String>> actions) {
		ArrayList<Set<String>> planExtract = new ArrayList<>();
		for (HashSet<String> action : actions) {
			Set<String> layerActions = new HashSet<>(action);
			planExtract.add(layerActions);
		}
		String pathTrace = planExtract.toString();
		pathTrace = pathTrace.replaceAll("\\[", "(");
		pathTrace = pathTrace.replaceAll("\\]", ")");
		pathTrace = '[' + pathTrace.substring(1, pathTrace.length() - 1) + ']';
		System.out.println(pathTrace);
	}

	 /**
	  * Method the extract the plan.
	  *
	  * @param currentLayer: current layer of the planning graph
	  * @param currentGoal: goal state to back track
	  * @param goalTrigger: previous trigger which lead to goal in current layer
	  */
	 public static void extractPlan(int currentLayer, HashSet<String> currentGoal, HashSet<String> goalTrigger) {
	 	if (currentLayer == 0 && !solutionFound) {
	 		logPlanExtract(actionTrace);
	 		solutionFound = true;
	 	}
	 	else {
	 		if (currentGoal.size() == 0) {
	 			extractPlan(currentLayer - 1, goalTrigger, new HashSet<>());
	 		}
	 		else {
	 			for (StateNode state: stateNodes.get(currentLayer).values()) {
	 				if (currentGoal.contains(state.nodeName)) {
	 					for (ActionNode preAct: state.preAction) {
	 						boolean hasMutex = false;
	 						for (String action: actionTrace.get(currentLayer - 1)) {
	 							if (actionsMutex.get(currentLayer - 1).contains(action + preAct.actionName)) {
	 								hasMutex = true;
	 								break;
	 							}
	 						}
	 						if (!hasMutex) {
	 							currentGoal.remove(state.nodeName);
	 							for (StateNode preState: preAct.preConditions) {
	 								goalTrigger.add(preState.nodeName);
	 							}
	 							actionTrace.get(currentLayer - 1).add(preAct.actionName);
	 							extractPlan(currentLayer, currentGoal, goalTrigger);
	 							actionTrace.get(currentLayer - 1).remove(preAct.actionName);
	 							currentGoal.add(state.nodeName);
	 							for (StateNode preState: preAct.preConditions) {
	 								goalTrigger.remove(preState.nodeName);
	 							}
	 						}
	 					}
	 				}
	 			}
	 		}
	 	}
	 }

	/**
	 * Method to check if we can perform an action or not based on the mutexes and availability of pre-conditions.
	 *
	 * @param layer: layer number
	 * @param action: action to be performed
	 * @return boolean value
	 */
	public static boolean checkMutexInPreCond(int layer, Action action){
		boolean performAction = true;
		for (int firstPreConditionIndex = 0; firstPreConditionIndex < action.preConditions.length && performAction;
			 firstPreConditionIndex++) {
			if (stateNodes.get(layer).containsKey(action.preConditions[firstPreConditionIndex])) {
				if (layer != 0) {
					for (int secondPreConditionIndex = 0; secondPreConditionIndex < firstPreConditionIndex
							&& performAction; secondPreConditionIndex++) {
						if (statesMutex.get(layer).contains(action.preConditions[firstPreConditionIndex]
								+ action.preConditions[secondPreConditionIndex])
								|| statesMutex.get(layer).contains(action.preConditions[secondPreConditionIndex]
								+ action.preConditions[firstPreConditionIndex]))
							performAction = false;
						break;
					}
				}
			}
			else {
				performAction = false;
			}
		}
		return performAction;
	}

	/**
	 * Method to make connections with states and the actions.
	 *
	 * @param layer: layer number
	 * @param action: action to be performed
	 */
	public static void makeConnectionsToActions(int layer, Action action){
		ActionNode actionNode = new ActionNode(action.actionName);
		actionNodes.get(layer).put(action.actionName, actionNode);
		stateNodes.add(new HashMap<>());

		// Establish connections between pre-states and actions.
		for (String preConditionName: action.preConditions) {
			StateNode preState = stateNodes.get(layer).get(preConditionName);
			preState.postAction.add(actionNode);
			actionNode.preConditions.add(preState);
		}

		// Establish connections between actions and post-states.
		for (String postEffectName: action.effects) {
			StateNode postState;
			if (!stateNodes.get(layer + 1).containsKey(postEffectName)) {
				postState = new StateNode(postEffectName);
				stateNodes.get(layer + 1).put(postEffectName, postState);
			}
			else postState = stateNodes.get(layer + 1).get(postEffectName);

			actionNode.postEffects.add(postState);
			postState.preAction.add(actionNode);
		}
	}

	/**
	 * Method to make connections to persist actions.
	 *
	 * @param layer: layer number
	 */
	public static void makeConnectionsToPersistActions(int layer){
		for (String persistentState: stateNodes.get(layer).keySet()) {
			StateNode postState;
			if (!stateNodes.get(layer + 1).containsKey(persistentState)) {
				postState = new StateNode(persistentState);
			}
			else {
				postState = stateNodes.get(layer + 1).get(persistentState);
			}
			ActionNode actPersistentNode = new ActionNode("persist("+persistentState+")");
			stateNodes.get(layer).get(persistentState).postAction.add(actPersistentNode);
			actPersistentNode.preConditions.add(stateNodes.get(layer).get(persistentState));
			actPersistentNode.postEffects.add(postState);
			postState.preAction.add(actPersistentNode);
			stateNodes.get(layer + 1).put(postState.nodeName, postState);
			actionNodes.get(layer).put("persist("+persistentState+")", actPersistentNode);
		}
	}

	/**
	 * Method to make connections between states and actions.
	 *
	 * @param layer: layer number
	 */
	public static void makeConnections(int layer){
		// Establish connections between states and action specified in pddl input.
		for (Action action: actions) {
			boolean performAction = checkMutexInPreCond(layer, action);

			if (performAction) {
				makeConnectionsToActions(layer, action);
			}
		}
		// Establish connections between states and the persist actions.
		makeConnectionsToPersistActions(layer);

		// log the action and state nodes generates in the planning graph.
		logActions(actionNodes.get(layer));
		System.out.println();
		logStates(stateNodes.get(layer + 1));
		System.out.println();
	}

	/**
	 * Method to mark competetive needs mutex type.
	 *
	 * @param layer: layer number
	 * @param actionOne: first action to compare
	 * @param actionTwo: second action to compare
	 */
	public static void markCNMutex(int layer, ActionNode actionOne, ActionNode actionTwo){
		for (StateNode preConditionOne: actionOne.preConditions)
			for (StateNode preConditionTwo: actionTwo.preConditions) {
				if (statesMutex.get(layer).contains(preConditionOne.nodeName + preConditionTwo.nodeName)) {
					actionsMutex.get(layer).add(actionOne.actionName + actionTwo.actionName);
					if (!cnMutex.contains(actionTwo.actionName + "," + actionOne.actionName))
						cnMutex.add(actionOne.actionName + "," + actionTwo.actionName);
				}
			}
	}

	/**
	 * Method to mark inconsistent effect mutex type.
	 *
	 * @param layer: layer number
	 * @param actionOne: first action to compare
	 * @param actionTwo: second action to compare
	 */
	public static void markIEMutex(int layer, ActionNode actionOne, ActionNode actionTwo){
		for (StateNode postEffectOne: actionOne.postEffects)
			for (StateNode postEffectTwo: actionTwo.postEffects) {
				if (postEffectOne.nodeName.substring(1).equals(postEffectTwo.nodeName)||
						postEffectTwo.nodeName.substring(1).equals(postEffectOne.nodeName)) {
					actionsMutex.get(layer).add(actionOne.actionName + actionTwo.actionName);
					if (!ieMutex.contains(actionTwo.actionName + "," + actionOne.actionName))
						ieMutex.add(actionOne.actionName + "," + actionTwo.actionName);
				}
			}
	}

	/**
	 * Method to mark interference mutex type.
	 *
	 * @param layer: layer number
	 * @param actionOne: first action to compare
	 * @param actionTwo: second action to compare
	 */
	public static void markIMutex(int layer, ActionNode actionOne, ActionNode actionTwo){
		for (StateNode preConditionOne: actionOne.preConditions)
			for (StateNode postEffectTwo: actionTwo.postEffects) {
				if (preConditionOne.nodeName.substring(1).equals(postEffectTwo.nodeName)||
						postEffectTwo.nodeName.substring(1).equals(preConditionOne.nodeName))  {
					actionsMutex.get(layer).add(actionOne.actionName + actionTwo.actionName);
					if (!iMutex.contains(actionTwo.actionName + "," + actionOne.actionName))
						iMutex.add(actionOne.actionName + "," + actionTwo.actionName);
				}
			}
		for (StateNode postEffectOne: actionOne.postEffects)
			for (StateNode preConditionTwo: actionTwo.preConditions) {
				if (postEffectOne.nodeName.substring(1).equals(preConditionTwo.nodeName)||
						preConditionTwo.nodeName.substring(1).equals(postEffectOne.nodeName))  {
					actionsMutex.get(layer).add(actionOne.actionName + actionTwo.actionName);
					if (!iMutex.contains(actionTwo.actionName + "," + actionOne.actionName))
						iMutex.add(actionOne.actionName + "," + actionTwo.actionName);
				}
			}
	}

	/**
	 * Method to mark action mutexes.
	 *
	 * @param layer: layer number
	 */
	public static void markActionMutexes(int layer){
		actionsMutex.add(new HashSet<String>());
		for (ActionNode actionOne: actionNodes.get(layer).values()) {
			for (ActionNode actionTwo: actionNodes.get(layer).values()) {
				if (actionOne.actionName.equals(actionTwo.actionName)){
					continue;
				}
				markCNMutex(layer, actionOne, actionTwo);
				markIEMutex(layer, actionOne, actionTwo);
				markIMutex(layer, actionOne, actionTwo);
			}
		}
		logMutexes(cnMutex, "CN");
		logMutexes(ieMutex, "IE");
		logMutexes(iMutex, "I");
	}

	/**
	 * Method to check for an inconsistent support.
	 *
	 * @param layer: layer number
	 * @param stateOne: first state to compare
	 * @param stateTwo: second state to compare
	 * @return boolean value
	 */
	public static boolean isInCosistentSupport(int layer, StateNode stateOne, StateNode stateTwo){
		boolean isInConsitentSupport = true;
		for (ActionNode preConditionOne: stateOne.preAction) {
			for (ActionNode preConditionTwo: stateTwo.preAction) {
				if (!actionsMutex.get(layer).contains(preConditionOne.actionName + preConditionTwo.actionName)
						&& !actionsMutex.get(layer).contains(preConditionTwo.actionName + preConditionOne.actionName)) {
					isInConsitentSupport = false;
					break;
				}
			}
		}
		return isInConsitentSupport;
	}

	/**
	 * Method to marks state mutexes.
	 *
	 * @param layer: layer number
	 */
	public static void markStateMutexes(int layer){
		statesMutex.add(new HashSet<String>());
		for (StateNode stateOne: stateNodes.get(layer+1).values()) {
			for (StateNode stateTwo: stateNodes.get(layer+1).values()) {
				if (stateOne.nodeName.equals(stateTwo.nodeName)){
					continue;
				}
				// Marks the negative literals.
				if (stateOne.nodeName.substring(1, stateOne.nodeName.length()).equals(stateTwo.nodeName)
						|| stateTwo.nodeName.substring(1, stateTwo.nodeName.length()).equals(stateOne.nodeName)) {
					statesMutex.get(layer + 1).add(stateOne.nodeName + stateTwo.nodeName);
					if (!nlMutex.contains(stateTwo.nodeName + "," + stateOne.nodeName))
						nlMutex.add(stateOne.nodeName + "," + stateTwo.nodeName);
				}
				// Marks the InConsitent Supports.
				else {
					boolean isInConsitentSupport = isInCosistentSupport(layer, stateOne, stateTwo);
					if (isInConsitentSupport) {
						statesMutex.get(layer + 1).add(stateOne.nodeName + stateTwo.nodeName);
						if (!isMutex.contains(stateTwo.nodeName + "," + stateOne.nodeName))
							isMutex.add(stateOne.nodeName + "," + stateTwo.nodeName);
					}
				}
			}
		}
		logMutexes(nlMutex, "NL");
		logMutexes(isMutex, "IS");
	}

	/**
	 * Method to check if a plan extract is possible.
	 *
	 * @param layer: layer number
	 * @return boolean value
	 */
	public static boolean canExtract(int layer){
		boolean isExtractPossible = true;
		for (String goalOne: goalState) {
			if (!stateNodes.get(layer + 1).containsKey(goalOne)){
				isExtractPossible = false;
			}
			else {
				for (String goalTwo: goalState)
					if (statesMutex.get(layer + 1).contains(goalOne + goalTwo)){
						isExtractPossible = false;
					}
			}
			if (!isExtractPossible) {
				break;
			}
		}
		return isExtractPossible;
	}

	/**
	 * Driver method to create a planning graph and extract a plan out of it.
	 *
	 * @param args: command line arguments
	 */
	public static void main(String[] args) {

		// parses the input from the input file.
		parseInput(args[0]);

		// prepares initial state with all the predicates.
		makeInitialState();

		// Expanding the planning graph.
		int layer = 0;
		boolean solution = false;
		boolean levelOff = false;
		boolean nextLevel = false;

		while (!solution && !levelOff) {
			System.out.print("Creating Layer = A");
			System.out.println(layer + 1);
			actionNodes.add(new HashMap<>());
			stateNodes.add(new HashMap<>());

			// Make connections between actions and states.
			makeConnections(layer);

			// Mark mutexes for all the action nodes.
			cnMutex = new HashSet<>();
			ieMutex = new HashSet<>();
			iMutex =  new HashSet<>();
			markActionMutexes(layer);

			// Mark mutexes for all the state nodes.
			nlMutex = new HashSet<>();
			isMutex = new HashSet<>();
			markStateMutexes(layer);

			// Check if plan extract is possible and generate plan if possible.
			boolean isExtractPossible = canExtract(layer);
			if (isExtractPossible) {
				System.out.println();
				System.out.println("Plan Extract:");
				for (int i = 0; i < layer + 1; i++) {
					actionTrace.add(new HashSet<>());
				}
				extractPlan(layer + 1, goalState, new HashSet<>());
				if (solutionFound) {
					solution = true;
				}
			}
			if ((stateNodes.get(layer + 1).size() == stateNodes.get(layer).size()) &&
					(statesMutex.get(layer + 1).size() == statesMutex.get(layer).size())) {
				levelOff = true;
			}
			layer++;
		}

		if (levelOff){
			System.out.println("Two consecutive layers are identical. The graph is Leveled Off!");
		}
	}
}

/**
 * Class structure to maintain a state node with its pre-actions and post-actions.
 */
class StateNode {
	String nodeName;
	ArrayList<ActionNode> preAction;
	ArrayList<ActionNode> postAction;

	/**
	 * Constructor to initialize state node.
	 *
	 * @param nodeName: name of the node
	 */
	StateNode(String nodeName){
		this.nodeName = nodeName;
		this.preAction = new ArrayList<>();
		this.postAction = new ArrayList<>();
	}
}

/**
 * Class structure to store an action with its pre-conditions and effects.
 */
class Action {
	String actionName;
	String[] preConditions;
	String[] effects;

	/**
	 * Constructor to initialize action.
	 *
	 * @param actionName: action name
	 * @param preConditions: preConditions for the action to execute
	 * @param effects: effects of the action
	 */
	Action(String actionName, String[] preConditions, String[] effects){
		this.actionName = actionName;
		this.preConditions = preConditions;
		this.effects = effects;
	}
}

/**
 * Class structure to maintain action node with its pre-conditions and post effects.
 */
class ActionNode {
	String actionName;
	ArrayList<StateNode> preConditions;
	ArrayList<StateNode> postEffects;

	/**
	 * Constructor to initialize action node.
	 *
	 * @param actionName: action name
	 */
	ActionNode(String actionName){
		this.actionName = actionName;
		preConditions = new ArrayList<>();
		postEffects = new ArrayList<>();
	}
}
