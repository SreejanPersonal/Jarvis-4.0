# Code Refactoring Guidelines for `voice\dialog\providers\gemini_live`

I need you to perform a comprehensive code refactoring operation on all files within the `voice\dialog\providers\gemini_live` directory/file. Your task involves carefully analyzing each file and implementing a more modular structure while preserving all existing functionality.

## Primary Objectives

1. Thoroughly examine every single file within the `voice\dialog\providers\gemini_live` directory/file
2. Identify files exceeding 60-70 lines of code for refactoring
3. Break larger files into multiple smaller, focused files
4. Organize these files into appropriate folders (existing or new)
5. Maintain the exact same functionality and logic throughout

## Refactoring Rules

### File Size Management
- Target files exceeding 60-70 lines of code for refactoring
- Do NOT split files that are already under this threshold
- Use professional judgment when a file is only slightly over the limit (e.g., 72-75 lines) if splitting would create unnecessary complexity

### Folder Organization
- Place refactored files in logically appropriate folders
- Create new folders when necessary to maintain clean organization
- You may use existing folders if they align with the file's purpose
- Ensure the folder structure reflects a professional, maintainable architecture

### Code Style Requirements
- **CRITICAL**: Do NOT include ANY comments in the code
- Docstrings are permitted and encouraged for documenting purpose
- Maintain the existing coding style and patterns
- Do not introduce new coding conventions

### Preservation Requirements
- **ABSOLUTELY CRUCIAL**: Do not alter ANY existing logic
- The refactored code must function identically to the original
- Do not modify any code outside the specified `voice\dialog\providers\gemini_live`
- Only remove code if you are 100% certain it is unused and disruptive

## File Structure Requirements
- Do NOT create `__init__` files in the new structure
- Ensure imports are properly updated to reflect new file locations
- Maintain proper dependency relationships between files

## Cleanup Requirements
- After successfully refactoring a file, delete the original file
- Remove any folders that become empty as a result of refactoring
- Delete any files or folders that are no longer needed after refactoring
- **IMPORTANT**: Only delete original files/folders after confirming that ALL functionality has been properly transferred to the new structure
- Be 100% certain that the refactored code completely replaces the original before deleting anything
- Clearly verify the imports in the refactored files.
- Clearly verify the relative imports in the refactored files.
- Try your best, That you don't need to change the imports in other files beyond the scope of the refactored files. The imports should be handled in such a way that you don't need to change the imports in other files beyond the scope of the refactored files.

## Scope Limitation
- Only work within the `voice\dialog\providers\gemini_live` directory/file
- Do not touch or modify any code outside this directory
- Focus exclusively on restructuring without changing behavior

Remember that the goal is to create a more maintainable codebase by breaking down large files into smaller, focused components while preserving all existing functionality. Your changes should make future development easier without introducing any behavioral changes or bugs.
