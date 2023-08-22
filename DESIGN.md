# Design Document for "Dungeon Master AI" (DMGPT)

## Introduction

This project aims to assist dungeon masters (DMs) in role-playing games (RPGs) like Dungeons & Dragons. Given the high stress and numerous responsibilities of a DM, this tool will alleviate some of their burdens and streamline the role-playing experience.

## Goals

### High Priority:

1. **LLM Dungeon Master (Assistant)**:
    - A digital assistant to guide and suggest moves for the DM.
    - Capable of suggesting plot points, character interactions, and potential outcomes.

2. **Object Representation for Characters, Places, and Things**:
    - An abstract representation to manage characters, locations, and items.
    - CRUD functionality for these objects: Create, Read, Update, Delete.

3. **User Interface Design**:
    - A clean and intuitive design to interact with the application.
    - While the coding of the interface is not required, wireframes or mock-ups should be provided.

### Medium Priority:

4. **Platforms**:
    - Support for Windows, Linux, and macOS.
    - Ensure consistent user experience across all platforms.

5. **Game Systems**:
    - Compatibility with Call of Cthulhu and D20 games.
    - Must be flexible to add support for other RPG systems in the future.

6. **Integration with Speech-to-Text Services**:
    - This will allow DMs to dictate actions and get responses, creating a dynamic storytelling experience.

### Low Priority:

7. **Text to Voice Integration**:
    - Enhance accessibility and offer an alternative way for users to interact with the system.

8. **THE GAME MASTER**:
    - The AI would be a full fledged Game Master and be able to run a game with little to no interference.

## Issues

1. **GPT Memory and Context**:
    - The GPT model may lose context after 10 texts. This could lead to inconsistent or inaccurate suggestions. Potential solutions include chunking information or creating a context manager.

## Development Process

- **Meetings**:
  - Team meetings will be held every two weeks to discuss progress, address issues, and plan for the next sprint.

- **Release Schedule**:
  - Version releases are planned once a month. Each release will incorporate feedback from the previous version and add new features as per the priority list.

## Conclusion

The "Dungeon Master AI" aims to provide a comprehensive tool for Dungeon Masters, easing their responsibilities and enhancing the gaming experience. This document lays out the project's initial design and goals. As development progresses, this design might evolve based on feedback and technical challenges.
