# Stable Matching Algorithm

## Purpose

The **Stable Matching Algorithm**, also known as the **Gale-Shapley algorithm**, solves the **Stable Marriage Problem**. The problem involves matching two sets of participants (typically referred to as proposers and receivers), where each participant has ranked the members of the opposite set based on preference. The goal is to find a **stable matching**, where there are no two participants who would prefer to be matched with each other over their current partners.

### A matching is stable if:
- No proposer and receiver would rather be matched with each other than with their current partners.
- A "pair" where two participants prefer each other over their current matches doesn't exist.

## Theory

The Stable Matching Algorithm was introduced by **David Gale** and **Lloyd Shapley** in 1962. It guarantees the existence of a stable matching for any set of preferences and provides an efficient way to find one.

- The algorithm works by allowing proposers to "propose" to their most preferred receivers in order. Receivers either accept or reject these proposals based on their preferences.
- The key insight is that proposers may be rejected, but eventually, each proposer will find a stable match.

The algorithm is **guaranteed to converge in O(N^2)** time, where **N** is the number of proposers (or receivers), and it results in a **stable matching** that is optimal for proposers (i.e., they get the best match possible given the constraints).

## Preconditions on Inputs

Before using the **Stable Matching Algorithm**, the following conditions must be satisfied for the inputs:

1. **Matching Groups**
   - There must be two groups: proposers and receivers.
   - Each proposer should be able to propose to any receiver, and each receiver should have a preference list of proposers.

2. **Preference Lists**
   - Both **proposer preferences** and **receiver preferences** should be provided as dictionaries, where:
     - **Proposer Preferences**: A dictionary where the keys are proposers, and the values are lists of receivers ranked in order of preference (with index 0 being the most preferred).
     - **Receiver Preferences**: A dictionary where the keys are receivers, and the values are lists of proposers ranked in order of preference.
   - The lists for each proposer and receiver must contain all members of the opposite set, i.e.,:
     - Each **proposer's list** must include all receivers.
     - Each **receiver's list** must include all proposers.
   
3. **No Missing Participants**
   - Every proposer and receiver should appear in the preference lists of the opposite group. Missing participants in the input data will result in a `ValueError`.

4. **Valid Preferences**
   - The preference lists should not be empty. Every proposer and receiver must have a valid list of preferences (at least one).
   - The lists should only contain valid participants from the opposite group (i.e., proposers in the receiver list and vice versa).

## What It's Used For

The Stable Matching Algorithm is used to solve real-world problems where two groups need to be matched, and each participant has preferences. Some notable applications include:

- **Matching jobs to candidates**: In systems such as medical residency programs, where candidates (students) are matched with hospitals (receivers).
- **Matching students to schools**: For example, school choice programs that assign students to schools based on preference rankings.
- **Organ donation**: Matching kidney donors with recipients based on compatibility and preference lists.
- **Marketplaces and Auctions**: Used in various markets, such as stock exchanges or marketplace platforms, to ensure optimal matching of buyers and sellers.

## Optimizations

The **Stable Matching Algorithm** can be optimized in the following ways:

### 1. **Keeping Track of the Next Receiver**

- To avoid unnecessary checks, each proposer maintains a pointer (or index) to the next receiver they will propose to. This reduces the work of having proposers iterate through their entire preference list every time they propose.

### 2. **Reverse Preference List with Ranking**

- A **reverse preference list** is used for each receiver. This list allows the algorithm to quickly compare proposers based on their rank for each receiver, speeding up the decision-making process during each proposal.
- Instead of comparing the proposers one by one, the reverse preference list allows checking whether a proposer is more favored than the receiver's current partner in constant time by simply looking up the index of the proposer in the list.

## Time Complexity

The time complexity of the **Stable Matching Algorithm** is **O(N^2)**, where **N** is the number of proposers (or receivers). This is because:
- Each proposer may propose to every receiver, resulting in **O(N)** proposals per proposer.
- Each proposal requires constant-time operations to either accept or reject the proposer, thanks to the precomputed rankings.

Thus, the overall complexity is **O(N^2)**. This time complexity makes the algorithm efficient for moderate-sized datasets but may not be optimal for extremely large matching problems.

## Applications

### 1. **Medical Residency Matching**
   - Medical schools and hospitals can use this algorithm to match graduating medical students with residency programs. Students and hospitals rank each other, and the Stable Matching Algorithm ensures a fair, efficient, and stable allocation of students to hospitals.

### 2. **College Admissions**
   - Many universities use variations of this algorithm to assign students to dorms or even to select research advisors. By maintaining a stable matching, both students and universities are satisfied with the results, as each participant gets an allocation they prefer, given the constraints.

### 3. **Organ Donation**
   - The algorithm can be used to match organ donors with recipients based on various preferences and medical compatibility criteria. By considering multiple factors, the Stable Matching Algorithm helps ensure that organs are allocated to the most suitable patients.

### 4. **Marketplaces and Auctions**
   - In markets where buyers and sellers are matched (like stock exchanges or marketplaces), the Stable Matching Algorithm can be applied to ensure efficient trading that is beneficial for all participants.

## Conclusion

The Stable Matching Algorithm is a powerful and widely applicable solution to the problem of matching participants based on preferences. By leveraging optimizations such as maintaining a reverse preference list with rankings and keeping track of the next receiver for each proposer, the algorithm efficiently finds stable and optimal matches. It is used in various real-world applications, from job markets to organ donation systems, providing fairness and stability in matching participants.
