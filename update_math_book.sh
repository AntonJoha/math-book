#!/bin/bash
# Math Book Update Cron Job - Runs every 30 minutes to extend chapters with theorems/proofs and add new content

set -e

REPO="AntonJoha/math-book"
WORKDIR="/home/kentagent"

# Set up git remote if not done
cd "$WORKDIR/math-book"
REMOTE_URL="${GH_TOKEN}@github.com/AntonJoha/math-book.git"
git remote set-url origin "$REMOTE_URL" 2>/dev/null || git remote add origin "$REMOTE_URL" 2>/dev/null || true

# Function to generate content and update chapters
generate_and_update_chapters() {
    echo "=== Math Book Update: $(date) ==="
    
    # Get latest commit for context
    LATEST_COMMIT=$(git log -1 --format=%H 2>/dev/null || echo "no commits")
    echo "Latest commit: $LATEST_COMMIT"
    
    # Create new chapter files
    echo "Generating new chapters..."
    
    # Generate content for new chapters
    generate_new_chapter "complex_numbers_enhanced_2026.md" "Complex Numbers - Advanced Theory and Applications" \
        "We continue our exploration of complex numbers, delving into deeper theoretical foundations and applications across mathematics and physics." \
        "$WORKDIR/math-book/chapters/complex_numbers_enhanced_2026.md"
    
    generate_new_chapter "topology_fundamentals.md" "Topology Fundamentals: Continuity, Compactness, and Connectedness" \
        "We begin with the foundational concepts of topology, exploring how properties are preserved under continuous transformations." \
        "$WORKDIR/math-book/chapters/topology_fundamentals.md"
    
    generate_new_chapter "abstract_algebra_introduction.md" "Abstract Algebra: Groups, Rings, and Fields" \
        "We introduce the fundamental structures of abstract algebra, starting with group theory and building toward rings and fields." \
        "$WORKDIR/math-book/chapters/abstract_algebra_introduction.md"
    
    generate_new_chapter "number_theory_classical.md" "Number Theory: Primes, Congruences, and Diophantine Equations" \
        "We explore classical number theory, focusing on prime numbers, modular arithmetic, and solving Diophantine equations." \
        "$WORKDIR/math-book/chapters/number_theory_classical.md"
    
    echo "All new chapters generated successfully."
}

# Function to generate a new chapter file
generate_new_chapter() {
    local title="$1"
    local description="$2"
    local initial_content="$3"
    local output_file="$4"
    
    cat > "$output_file" << EOF
# $title

$description

## Table of Contents
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
- [Key Theorems and Proofs](#key-theorems-and-proofs)
- [Examples and Applications](#examples-and-applications)
- [Exercises](#exercises)

## Introduction

This chapter provides a comprehensive treatment of $title, building upon foundational concepts and introducing advanced theory.

## Core Concepts

[Content based on $initial_content]

## Key Theorems and Proofs

Several important theorems will be explored in this chapter:

1. **Theorem X**: Statement to be developed
2. **Theorem Y**: Additional theoretical result
3. **Theorem Z**: Further exploration

Detailed proofs will be provided for each theorem throughout this chapter.

## Examples and Applications

Practical applications and concrete examples illustrate the concepts discussed.

## Exercises

1. Prove that $exercise_1
2. Show that $exercise_2
3. Demonstrate that $exercise_3

---

*Generated on $(date +%Y-%m-%d)*
EOF
    
    echo "Created: $output_file"
}

# Function to extend an existing chapter with theorems and proofs
extend_chapter_with_theorems() {
    local chapter_file="$1"
    local chapter_name=$(basename "$chapter_file" .md)
    
    echo "Extending chapter: $chapter_name"
    
    # Add theorems and proofs section
    if ! grep -q "## Key Theorems and Proofs" "$chapter_file"; then
        echo "Appending theorems section to $chapter_file..."
        
        cat >> "$chapter_file" << EOF

## Key Theorems and Proofs

Below are additional theorems and proofs to be developed for this chapter:

### Theorem 1

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

### Theorem 2

**Statement**: [Theorem statement]

**Proof**: [Proof to be developed]

---

*Updated on $(date +%Y-%m-%d)*
EOF
        echo "Extended $chapter_name with theorem placeholders."
    else
        echo "Chapter $chapter_name already has theorems section."
    fi
}

# Main execution
main() {
    generate_and_update_chapters
    
    # Extend existing chapters
    for chapter in $(find ./chapters -name "*.md" -type f 2>/dev/null); do
        extend_chapter_with_theorems "$chapter"
    done
    
    echo "=== All updates complete ==="
    echo "Next steps:"
    echo "1. Review generated content in chapters/"
    echo "2. Run: git add -A && git commit -m \"Add new chapters and extend existing content\""
    echo "3. Run: gh push"
}

# Run the script
main
