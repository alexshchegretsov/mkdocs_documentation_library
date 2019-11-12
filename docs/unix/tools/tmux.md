`tmux`
=

tmux - terminal multiplexor

- `tmux new-session -s [new_session_name]` - create new session
- `ctrl+B D` - detach from session
- `tmux attach -t [session_name]` - attach to session
- `ctrl+B shft+;(:)` enter kill-session - kill session
- `ctrl+B C` - create new window
- `ctrl+B 0` - switch to 0 window
- `ctrl+B 1` - switch to 1 window
- `ctrl+B shft+5(%)` - divide window by 2 vertical halfs
- `ctrl+B left` - switch to left half
- `ctrl+B right` - switch to right half
- `ctrl+b shift+"` - divide window by 2 horizontal half
- `ctrl+b up` - switch to up half
- `ctrl+b down` - switch to down half

#### copy - paste

- `ctrl+b [` - enter copy mode
- `ctrl+space` - start select
- `alt+w` - copy selected area
- `ctrl+b + ]` - paste
