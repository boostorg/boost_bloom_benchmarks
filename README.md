# Performance of [Boost.Bloom](https://github.com/boostorg/bloom) bulk operations

The tables show the relative performance of bulk insertion and bulk lookup
operations with respect to their regular equivalents: figures greater than 1.0 mean
bulk operations are faster.

We test several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.85</td>
    <td align="right">0.67</td>
    <td align="right">2.17</td>
    <td align="right">1.45</td>
    <td align="center">4</td>
    <td align="right">1.27</td>
    <td align="right">1.15</td>
    <td align="right">1.17</td>
    <td align="right">1.26</td>
    <td align="center">5</td>
    <td align="right">1.12</td>
    <td align="right">1.23</td>
    <td align="right">1.25</td>
    <td align="right">1.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.82</td>
    <td align="right">0.68</td>
    <td align="right">2.21</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">1.14</td>
    <td align="right">1.31</td>
    <td align="right">1.19</td>
    <td align="right">1.22</td>
    <td align="center">6</td>
    <td align="right">1.08</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.82</td>
    <td align="right">0.69</td>
    <td align="right">2.16</td>
    <td align="right">1.11</td>
    <td align="center">6</td>
    <td align="right">1.22</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="center">7</td>
    <td align="right">1.14</td>
    <td align="right">1.20</td>
    <td align="right">1.30</td>
    <td align="right">1.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.76</td>
    <td align="right">0.69</td>
    <td align="right">2.17</td>
    <td align="right">0.97</td>
    <td align="center">7</td>
    <td align="right">1.26</td>
    <td align="right">1.22</td>
    <td align="right">1.19</td>
    <td align="right">1.21</td>
    <td align="center">8</td>
    <td align="right">1.09</td>
    <td align="right">1.26</td>
    <td align="right">1.28</td>
    <td align="right">1.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.25</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.36</td>
    <td align="center">5</td>
    <td align="right">1.13</td>
    <td align="right">1.55</td>
    <td align="right">1.51</td>
    <td align="right">1.53</td>
    <td align="center">5</td>
    <td align="right">1.02</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.19</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">1.26</td>
    <td align="right">1.72</td>
    <td align="right">1.72</td>
    <td align="right">1.71</td>
    <td align="center">8</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
    <td align="right">0.95</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.26</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="right">1.69</td>
    <td align="center">11</td>
    <td align="right">0.92</td>
    <td align="right">1.72</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">1.13</td>
    <td align="right">1.23</td>
    <td align="right">1.32</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.29</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">14</td>
    <td align="right">1.26</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.81</td>
    <td align="center">13</td>
    <td align="right">1.13</td>
    <td align="right">1.24</td>
    <td align="right">1.25</td>
    <td align="right">1.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">0.99</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.17</td>
    <td align="center">5</td>
    <td align="right">1.14</td>
    <td align="right">1.25</td>
    <td align="right">1.15</td>
    <td align="right">1.17</td>
    <td align="center">5</td>
    <td align="right">1.12</td>
    <td align="right">1.17</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.03</td>
    <td align="right">1.08</td>
    <td align="right">1.11</td>
    <td align="right">1.10</td>
    <td align="center">8</td>
    <td align="right">1.09</td>
    <td align="right">1.15</td>
    <td align="right">1.17</td>
    <td align="right">1.15</td>
    <td align="center">8</td>
    <td align="right">1.08</td>
    <td align="right">1.19</td>
    <td align="right">1.17</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.97</td>
    <td align="right">1.23</td>
    <td align="right">1.31</td>
    <td align="right">1.22</td>
    <td align="center">11</td>
    <td align="right">0.93</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="center">11</td>
    <td align="right">0.92</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.97</td>
    <td align="right">1.23</td>
    <td align="right">1.30</td>
    <td align="right">1.23</td>
    <td align="center">13</td>
    <td align="right">1.15</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="center">14</td>
    <td align="right">1.04</td>
    <td align="right">1.12</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.26</td>
    <td align="right">1.32</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">6</td>
    <td align="right">0.90</td>
    <td align="right">1.40</td>
    <td align="right">1.45</td>
    <td align="right">1.45</td>
    <td align="center">7</td>
    <td align="right">1.12</td>
    <td align="right">1.37</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.29</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="right">1.29</td>
    <td align="center">7</td>
    <td align="right">0.88</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
    <td align="center">10</td>
    <td align="right">1.07</td>
    <td align="right">1.31</td>
    <td align="right">1.27</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.37</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="center">10</td>
    <td align="right">1.01</td>
    <td align="right">1.53</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="center">11</td>
    <td align="right">1.03</td>
    <td align="right">1.24</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.31</td>
    <td align="right">1.48</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">12</td>
    <td align="right">1.03</td>
    <td align="right">1.71</td>
    <td align="right">1.72</td>
    <td align="right">1.72</td>
    <td align="center">15</td>
    <td align="right">0.98</td>
    <td align="right">1.22</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.14</td>
    <td align="right">0.91</td>
    <td align="right">2.19</td>
    <td align="right">1.46</td>
    <td align="center">4</td>
    <td align="right">1.34</td>
    <td align="right">1.26</td>
    <td align="right">1.30</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.27</td>
    <td align="right">1.31</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.84</td>
    <td align="right">1.60</td>
    <td align="right">2.26</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">2.03</td>
    <td align="right">2.06</td>
    <td align="right">1.99</td>
    <td align="right">2.02</td>
    <td align="center">6</td>
    <td align="right">1.80</td>
    <td align="right">1.83</td>
    <td align="right">1.84</td>
    <td align="right">1.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.16</td>
    <td align="right">2.06</td>
    <td align="right">2.39</td>
    <td align="right">1.44</td>
    <td align="center">6</td>
    <td align="right">2.94</td>
    <td align="right">2.82</td>
    <td align="right">2.97</td>
    <td align="right">2.79</td>
    <td align="center">7</td>
    <td align="right">2.60</td>
    <td align="right">2.80</td>
    <td align="right">2.57</td>
    <td align="right">2.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">2.11</td>
    <td align="right">2.18</td>
    <td align="right">2.52</td>
    <td align="right">1.40</td>
    <td align="center">7</td>
    <td align="right">3.75</td>
    <td align="right">3.15</td>
    <td align="right">3.17</td>
    <td align="right">3.38</td>
    <td align="center">8</td>
    <td align="right">2.67</td>
    <td align="right">3.10</td>
    <td align="right">3.20</td>
    <td align="right">3.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">1.25</td>
    <td align="right">1.70</td>
    <td align="right">1.58</td>
    <td align="right">1.56</td>
    <td align="center">5</td>
    <td align="right">1.14</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
    <td align="right">1.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.99</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="right">2.16</td>
    <td align="center">8</td>
    <td align="right">2.23</td>
    <td align="right">2.56</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">8</td>
    <td align="right">2.00</td>
    <td align="right">2.02</td>
    <td align="right">1.88</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.18</td>
    <td align="right">2.56</td>
    <td align="right">2.56</td>
    <td align="right">2.52</td>
    <td align="center">11</td>
    <td align="right">1.69</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="center">11</td>
    <td align="right">2.73</td>
    <td align="right">3.04</td>
    <td align="right">2.99</td>
    <td align="right">3.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.05</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
    <td align="center">14</td>
    <td align="right">2.18</td>
    <td align="right">2.86</td>
    <td align="right">2.75</td>
    <td align="right">2.88</td>
    <td align="center">13</td>
    <td align="right">2.42</td>
    <td align="right">2.70</td>
    <td align="right">2.63</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.20</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="center">5</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">1.29</td>
    <td align="right">1.40</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.90</td>
    <td align="right">2.00</td>
    <td align="right">1.99</td>
    <td align="right">1.99</td>
    <td align="center">8</td>
    <td align="right">2.21</td>
    <td align="right">2.21</td>
    <td align="right">2.29</td>
    <td align="right">2.15</td>
    <td align="center">8</td>
    <td align="right">2.01</td>
    <td align="right">2.20</td>
    <td align="right">2.17</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.57</td>
    <td align="right">2.99</td>
    <td align="right">2.98</td>
    <td align="right">2.97</td>
    <td align="center">11</td>
    <td align="right">1.95</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
    <td align="right">2.14</td>
    <td align="center">11</td>
    <td align="right">1.82</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="right">2.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.31</td>
    <td align="right">2.60</td>
    <td align="right">2.61</td>
    <td align="right">2.62</td>
    <td align="center">13</td>
    <td align="right">1.76</td>
    <td align="right">1.90</td>
    <td align="right">1.89</td>
    <td align="right">1.90</td>
    <td align="center">14</td>
    <td align="right">1.69</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.37</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">1.03</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
    <td align="right">1.43</td>
    <td align="center">7</td>
    <td align="right">1.17</td>
    <td align="right">1.23</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.90</td>
    <td align="right">1.82</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="center">7</td>
    <td align="right">1.57</td>
    <td align="right">2.26</td>
    <td align="right">2.41</td>
    <td align="right">2.39</td>
    <td align="center">10</td>
    <td align="right">1.48</td>
    <td align="right">1.61</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">2.96</td>
    <td align="right">2.58</td>
    <td align="right">2.59</td>
    <td align="right">2.59</td>
    <td align="center">10</td>
    <td align="right">2.38</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
    <td align="right">3.33</td>
    <td align="center">11</td>
    <td align="right">1.35</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">3.45</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="right">3.22</td>
    <td align="center">12</td>
    <td align="right">3.17</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
    <td align="right">3.95</td>
    <td align="center">15</td>
    <td align="right">1.20</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
</table>

<!--gcc-x64/bulk_comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.79</td>
    <td align="right">0.65</td>
    <td align="right">2.37</td>
    <td align="right">1.54</td>
    <td align="center">4</td>
    <td align="right">1.39</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="right">1.25</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.79</td>
    <td align="right">0.65</td>
    <td align="right">2.41</td>
    <td align="right">1.31</td>
    <td align="center">5</td>
    <td align="right">1.39</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.26</td>
    <td align="center">6</td>
    <td align="right">1.22</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.76</td>
    <td align="right">0.67</td>
    <td align="right">2.35</td>
    <td align="right">1.14</td>
    <td align="center">6</td>
    <td align="right">1.39</td>
    <td align="right">1.30</td>
    <td align="right">1.34</td>
    <td align="right">1.31</td>
    <td align="center">7</td>
    <td align="right">1.14</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.74</td>
    <td align="right">0.65</td>
    <td align="right">2.36</td>
    <td align="right">1.01</td>
    <td align="center">7</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="center">8</td>
    <td align="right">0.99</td>
    <td align="right">0.96</td>
    <td align="right">0.99</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.09</td>
    <td align="right">1.27</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">1.05</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
    <td align="right">1.34</td>
    <td align="center">5</td>
    <td align="right">1.11</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.23</td>
    <td align="right">1.16</td>
    <td align="right">1.14</td>
    <td align="right">1.16</td>
    <td align="center">8</td>
    <td align="right">1.06</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="center">8</td>
    <td align="right">1.12</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="right">1.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.23</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
    <td align="right">1.40</td>
    <td align="center">11</td>
    <td align="right">1.21</td>
    <td align="right">1.36</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="center">11</td>
    <td align="right">1.14</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.19</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
    <td align="center">14</td>
    <td align="right">1.13</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="center">13</td>
    <td align="right">1.14</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.09</td>
    <td align="right">1.19</td>
    <td align="right">1.12</td>
    <td align="right">1.21</td>
    <td align="center">5</td>
    <td align="right">1.18</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.27</td>
    <td align="right">1.19</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.08</td>
    <td align="right">1.21</td>
    <td align="right">1.15</td>
    <td align="right">1.24</td>
    <td align="center">8</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="center">8</td>
    <td align="right">1.16</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.13</td>
    <td align="right">1.30</td>
    <td align="right">1.24</td>
    <td align="right">1.30</td>
    <td align="center">11</td>
    <td align="right">1.11</td>
    <td align="right">1.18</td>
    <td align="right">1.19</td>
    <td align="right">1.17</td>
    <td align="center">11</td>
    <td align="right">1.12</td>
    <td align="right">1.17</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.13</td>
    <td align="right">1.25</td>
    <td align="right">1.31</td>
    <td align="right">1.25</td>
    <td align="center">13</td>
    <td align="right">1.11</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="right">1.16</td>
    <td align="center">14</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.12</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.50</td>
    <td align="right">1.48</td>
    <td align="right">1.47</td>
    <td align="right">1.48</td>
    <td align="center">6</td>
    <td align="right">0.96</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.52</td>
    <td align="center">7</td>
    <td align="right">1.02</td>
    <td align="right">1.35</td>
    <td align="right">1.41</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.42</td>
    <td align="right">1.45</td>
    <td align="right">1.43</td>
    <td align="right">1.42</td>
    <td align="center">7</td>
    <td align="right">0.98</td>
    <td align="right">1.77</td>
    <td align="right">1.77</td>
    <td align="right">1.78</td>
    <td align="center">10</td>
    <td align="right">1.08</td>
    <td align="right">1.30</td>
    <td align="right">1.31</td>
    <td align="right">1.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.59</td>
    <td align="right">1.48</td>
    <td align="right">1.47</td>
    <td align="right">1.49</td>
    <td align="center">10</td>
    <td align="right">0.98</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">11</td>
    <td align="right">1.02</td>
    <td align="right">1.24</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.54</td>
    <td align="right">1.51</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">12</td>
    <td align="right">1.06</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="center">15</td>
    <td align="right">0.95</td>
    <td align="right">1.17</td>
    <td align="right">1.19</td>
    <td align="right">1.17</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.05</td>
    <td align="right">0.84</td>
    <td align="right">2.37</td>
    <td align="right">1.55</td>
    <td align="center">4</td>
    <td align="right">1.63</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">1.29</td>
    <td align="right">1.37</td>
    <td align="right">1.41</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.75</td>
    <td align="right">1.47</td>
    <td align="right">2.26</td>
    <td align="right">1.37</td>
    <td align="center">5</td>
    <td align="right">2.47</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="right">2.31</td>
    <td align="center">6</td>
    <td align="right">2.06</td>
    <td align="right">2.23</td>
    <td align="right">2.24</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.17</td>
    <td align="right">1.96</td>
    <td align="right">2.35</td>
    <td align="right">1.40</td>
    <td align="center">6</td>
    <td align="right">3.59</td>
    <td align="right">3.40</td>
    <td align="right">3.44</td>
    <td align="right">3.41</td>
    <td align="center">7</td>
    <td align="right">2.64</td>
    <td align="right">3.05</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">2.04</td>
    <td align="right">2.00</td>
    <td align="right">2.37</td>
    <td align="right">1.31</td>
    <td align="center">7</td>
    <td align="right">3.92</td>
    <td align="right">3.80</td>
    <td align="right">3.80</td>
    <td align="right">3.80</td>
    <td align="center">8</td>
    <td align="right">1.77</td>
    <td align="right">2.03</td>
    <td align="right">2.03</td>
    <td align="right">2.02</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.41</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="center">5</td>
    <td align="right">1.28</td>
    <td align="right">1.58</td>
    <td align="right">1.57</td>
    <td align="right">1.58</td>
    <td align="center">5</td>
    <td align="right">1.41</td>
    <td align="right">1.46</td>
    <td align="right">1.46</td>
    <td align="right">1.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">2.46</td>
    <td align="right">2.45</td>
    <td align="right">2.41</td>
    <td align="right">2.44</td>
    <td align="center">8</td>
    <td align="right">2.07</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
    <td align="center">8</td>
    <td align="right">2.42</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.66</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="right">1.95</td>
    <td align="center">11</td>
    <td align="right">1.55</td>
    <td align="right">1.86</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">11</td>
    <td align="right">2.33</td>
    <td align="right">2.70</td>
    <td align="right">2.69</td>
    <td align="right">2.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.49</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="right">1.89</td>
    <td align="center">14</td>
    <td align="right">1.51</td>
    <td align="right">1.89</td>
    <td align="right">1.88</td>
    <td align="right">1.88</td>
    <td align="center">13</td>
    <td align="right">1.85</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.38</td>
    <td align="right">1.46</td>
    <td align="right">1.44</td>
    <td align="right">1.48</td>
    <td align="center">5</td>
    <td align="right">1.37</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">1.39</td>
    <td align="right">1.55</td>
    <td align="right">1.49</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.98</td>
    <td align="right">2.08</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="center">8</td>
    <td align="right">2.64</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
    <td align="right">2.57</td>
    <td align="center">8</td>
    <td align="right">2.31</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.15</td>
    <td align="right">2.59</td>
    <td align="right">2.59</td>
    <td align="right">2.59</td>
    <td align="center">11</td>
    <td align="right">1.65</td>
    <td align="right">1.86</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">11</td>
    <td align="right">1.58</td>
    <td align="right">1.85</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.73</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="right">2.06</td>
    <td align="center">13</td>
    <td align="right">1.48</td>
    <td align="right">1.89</td>
    <td align="right">1.89</td>
    <td align="right">1.89</td>
    <td align="center">14</td>
    <td align="right">1.49</td>
    <td align="right">1.81</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.55</td>
    <td align="right">1.48</td>
    <td align="right">1.47</td>
    <td align="right">1.48</td>
    <td align="center">6</td>
    <td align="right">1.03</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="center">7</td>
    <td align="right">1.10</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">2.19</td>
    <td align="right">2.16</td>
    <td align="right">2.15</td>
    <td align="right">2.14</td>
    <td align="center">7</td>
    <td align="right">1.62</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="right">2.59</td>
    <td align="center">10</td>
    <td align="right">1.42</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">3.04</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
    <td align="right">2.93</td>
    <td align="center">10</td>
    <td align="right">2.28</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">11</td>
    <td align="right">1.32</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">3.63</td>
    <td align="right">3.38</td>
    <td align="right">3.35</td>
    <td align="right">3.36</td>
    <td align="center">12</td>
    <td align="right">3.27</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="right">4.13</td>
    <td align="center">15</td>
    <td align="right">1.21</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
  </tr>
</table>

<!--clang-x64/bulk_comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.83</td>
    <td align="right">0.47</td>
    <td align="right">2.78</td>
    <td align="right">1.84</td>
    <td align="center">4</td>
    <td align="right">0.88</td>
    <td align="right">0.83</td>
    <td align="right">0.83</td>
    <td align="right">0.84</td>
    <td align="center">5</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.82</td>
    <td align="right">0.47</td>
    <td align="right">2.76</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">0.89</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="right">0.90</td>
    <td align="center">6</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.82</td>
    <td align="right">0.48</td>
    <td align="right">2.67</td>
    <td align="right">1.29</td>
    <td align="center">6</td>
    <td align="right">0.95</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">7</td>
    <td align="right">0.90</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.82</td>
    <td align="right">0.48</td>
    <td align="right">2.69</td>
    <td align="right">1.11</td>
    <td align="center">7</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">0.97</td>
    <td align="right">0.95</td>
    <td align="right">0.96</td>
    <td align="right">0.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.00</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="center">5</td>
    <td align="right">0.98</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">1.09</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.14</td>
    <td align="right">0.90</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="center">8</td>
    <td align="right">1.08</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="center">8</td>
    <td align="right">1.05</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.16</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="center">11</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">11</td>
    <td align="right">1.07</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.18</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="right">1.14</td>
    <td align="center">14</td>
    <td align="right">1.12</td>
    <td align="right">1.07</td>
    <td align="right">1.07</td>
    <td align="right">1.09</td>
    <td align="center">13</td>
    <td align="right">1.07</td>
    <td align="right">1.05</td>
    <td align="right">1.06</td>
    <td align="right">1.05</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.08</td>
    <td align="right">1.06</td>
    <td align="right">1.07</td>
    <td align="right">1.06</td>
    <td align="center">5</td>
    <td align="right">1.03</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="center">5</td>
    <td align="right">0.98</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="right">1.10</td>
    <td align="right">1.09</td>
    <td align="center">8</td>
    <td align="right">1.14</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="right">0.89</td>
    <td align="center">8</td>
    <td align="right">1.07</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.06</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">11</td>
    <td align="right">1.17</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="center">11</td>
    <td align="right">1.13</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.06</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">13</td>
    <td align="right">1.19</td>
    <td align="right">1.13</td>
    <td align="right">1.14</td>
    <td align="right">1.13</td>
    <td align="center">14</td>
    <td align="right">1.17</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.00</td>
    <td align="right">1.31</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">6</td>
    <td align="right">1.26</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="center">7</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.97</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="center">7</td>
    <td align="right">1.23</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.30</td>
    <td align="center">10</td>
    <td align="right">1.15</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
    <td align="right">1.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.05</td>
    <td align="right">1.33</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
    <td align="center">10</td>
    <td align="right">1.16</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="center">11</td>
    <td align="right">1.14</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.09</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="center">12</td>
    <td align="right">1.17</td>
    <td align="right">1.40</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
    <td align="center">15</td>
    <td align="right">1.20</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.90</td>
    <td align="right">0.67</td>
    <td align="right">3.04</td>
    <td align="right">2.07</td>
    <td align="center">4</td>
    <td align="right">1.31</td>
    <td align="right">1.34</td>
    <td align="right">1.33</td>
    <td align="right">1.34</td>
    <td align="center">5</td>
    <td align="right">0.99</td>
    <td align="right">1.19</td>
    <td align="right">1.21</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.00</td>
    <td align="right">0.88</td>
    <td align="right">2.93</td>
    <td align="right">1.99</td>
    <td align="center">5</td>
    <td align="right">2.01</td>
    <td align="right">2.29</td>
    <td align="right">2.06</td>
    <td align="right">2.07</td>
    <td align="center">6</td>
    <td align="right">1.54</td>
    <td align="right">1.71</td>
    <td align="right">1.85</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.43</td>
    <td align="right">1.30</td>
    <td align="right">2.47</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">2.47</td>
    <td align="right">2.81</td>
    <td align="right">2.74</td>
    <td align="right">2.62</td>
    <td align="center">7</td>
    <td align="right">2.01</td>
    <td align="right">2.00</td>
    <td align="right">2.05</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">1.40</td>
    <td align="right">1.12</td>
    <td align="right">2.08</td>
    <td align="right">1.07</td>
    <td align="center">7</td>
    <td align="right">2.84</td>
    <td align="right">3.10</td>
    <td align="right">3.04</td>
    <td align="right">3.16</td>
    <td align="center">8</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.88</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.10</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="center">5</td>
    <td align="right">1.06</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
    <td align="right">1.32</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.90</td>
    <td align="right">2.09</td>
    <td align="right">1.96</td>
    <td align="right">2.27</td>
    <td align="center">8</td>
    <td align="right">1.49</td>
    <td align="right">2.02</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="center">8</td>
    <td align="right">1.77</td>
    <td align="right">2.27</td>
    <td align="right">2.30</td>
    <td align="right">2.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.07</td>
    <td align="right">2.08</td>
    <td align="right">2.11</td>
    <td align="right">1.97</td>
    <td align="center">11</td>
    <td align="right">2.10</td>
    <td align="right">2.20</td>
    <td align="right">2.23</td>
    <td align="right">2.04</td>
    <td align="center">11</td>
    <td align="right">2.17</td>
    <td align="right">2.49</td>
    <td align="right">2.58</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.06</td>
    <td align="right">2.21</td>
    <td align="right">2.10</td>
    <td align="right">2.26</td>
    <td align="center">14</td>
    <td align="right">2.16</td>
    <td align="right">2.34</td>
    <td align="right">2.41</td>
    <td align="right">2.34</td>
    <td align="center">13</td>
    <td align="right">2.01</td>
    <td align="right">2.48</td>
    <td align="right">2.58</td>
    <td align="right">2.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.49</td>
    <td align="right">1.46</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">1.11</td>
    <td align="right">1.31</td>
    <td align="right">1.33</td>
    <td align="right">1.30</td>
    <td align="center">5</td>
    <td align="right">1.06</td>
    <td align="right">1.34</td>
    <td align="right">1.33</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.38</td>
    <td align="right">1.64</td>
    <td align="right">1.57</td>
    <td align="right">1.65</td>
    <td align="center">8</td>
    <td align="right">2.15</td>
    <td align="right">2.10</td>
    <td align="right">2.27</td>
    <td align="right">2.10</td>
    <td align="center">8</td>
    <td align="right">1.51</td>
    <td align="right">2.02</td>
    <td align="right">1.97</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.33</td>
    <td align="right">2.43</td>
    <td align="right">2.45</td>
    <td align="right">2.45</td>
    <td align="center">11</td>
    <td align="right">2.04</td>
    <td align="right">2.18</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="center">11</td>
    <td align="right">2.00</td>
    <td align="right">2.20</td>
    <td align="right">2.16</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.97</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
    <td align="right">2.69</td>
    <td align="center">13</td>
    <td align="right">2.13</td>
    <td align="right">2.29</td>
    <td align="right">2.30</td>
    <td align="right">2.34</td>
    <td align="center">14</td>
    <td align="right">2.15</td>
    <td align="right">2.37</td>
    <td align="right">2.37</td>
    <td align="right">2.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.36</td>
    <td align="right">1.78</td>
    <td align="right">1.83</td>
    <td align="right">1.79</td>
    <td align="center">6</td>
    <td align="right">1.51</td>
    <td align="right">1.59</td>
    <td align="right">1.61</td>
    <td align="right">1.59</td>
    <td align="center">7</td>
    <td align="right">1.17</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.80</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="right">2.59</td>
    <td align="center">7</td>
    <td align="right">2.00</td>
    <td align="right">2.33</td>
    <td align="right">2.31</td>
    <td align="right">2.32</td>
    <td align="center">10</td>
    <td align="right">1.30</td>
    <td align="right">1.43</td>
    <td align="right">1.44</td>
    <td align="right">1.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">2.69</td>
    <td align="right">3.72</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">10</td>
    <td align="right">2.73</td>
    <td align="right">3.64</td>
    <td align="right">3.64</td>
    <td align="right">3.67</td>
    <td align="center">11</td>
    <td align="right">1.57</td>
    <td align="right">1.55</td>
    <td align="right">1.56</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">3.11</td>
    <td align="right">4.08</td>
    <td align="right">4.09</td>
    <td align="right">4.15</td>
    <td align="center">12</td>
    <td align="right">3.26</td>
    <td align="right">4.32</td>
    <td align="right">4.40</td>
    <td align="right">4.46</td>
    <td align="center">15</td>
    <td align="right">1.72</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
  </tr>
</table>

<!--clang-arm64/bulk_comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.09</td>
    <td align="right">0.66</td>
    <td align="right">1.88</td>
    <td align="right">1.21</td>
    <td align="center">4</td>
    <td align="right">1.44</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="center">5</td>
    <td align="right">1.40</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.03</td>
    <td align="right">0.64</td>
    <td align="right">1.87</td>
    <td align="right">1.00</td>
    <td align="center">5</td>
    <td align="right">1.47</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="center">6</td>
    <td align="right">1.44</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.01</td>
    <td align="right">0.67</td>
    <td align="right">1.85</td>
    <td align="right">0.88</td>
    <td align="center">6</td>
    <td align="right">1.49</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
    <td align="center">7</td>
    <td align="right">1.47</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">1.14</td>
    <td align="right">0.67</td>
    <td align="right">1.86</td>
    <td align="right">0.78</td>
    <td align="center">7</td>
    <td align="right">1.53</td>
    <td align="right">1.22</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">8</td>
    <td align="right">1.50</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.51</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="center">5</td>
    <td align="right">0.97</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="center">5</td>
    <td align="right">1.36</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
    <td align="right">0.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.63</td>
    <td align="right">1.49</td>
    <td align="right">1.48</td>
    <td align="right">1.49</td>
    <td align="center">8</td>
    <td align="right">0.95</td>
    <td align="right">1.17</td>
    <td align="right">1.16</td>
    <td align="right">1.17</td>
    <td align="center">8</td>
    <td align="right">1.59</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.62</td>
    <td align="right">1.49</td>
    <td align="right">1.48</td>
    <td align="right">1.46</td>
    <td align="center">11</td>
    <td align="right">1.14</td>
    <td align="right">1.58</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
    <td align="center">11</td>
    <td align="right">1.33</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.59</td>
    <td align="right">1.49</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">14</td>
    <td align="right">1.14</td>
    <td align="right">1.60</td>
    <td align="right">1.59</td>
    <td align="right">1.60</td>
    <td align="center">13</td>
    <td align="right">1.33</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.27</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="center">5</td>
    <td align="right">1.27</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">1.21</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.38</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="right">0.93</td>
    <td align="center">8</td>
    <td align="right">1.56</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
    <td align="center">8</td>
    <td align="right">1.26</td>
    <td align="right">1.15</td>
    <td align="right">1.14</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.32</td>
    <td align="right">1.07</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="center">11</td>
    <td align="right">1.54</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">11</td>
    <td align="right">1.40</td>
    <td align="right">1.37</td>
    <td align="right">1.36</td>
    <td align="right">1.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.31</td>
    <td align="right">1.08</td>
    <td align="right">1.09</td>
    <td align="right">1.08</td>
    <td align="center">13</td>
    <td align="right">1.38</td>
    <td align="right">1.34</td>
    <td align="right">1.37</td>
    <td align="right">1.36</td>
    <td align="center">14</td>
    <td align="right">1.38</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.36</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">6</td>
    <td align="right">1.03</td>
    <td align="right">1.23</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="center">7</td>
    <td align="right">1.23</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="right">1.32</td>
    <td align="center">7</td>
    <td align="right">1.15</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
    <td align="center">10</td>
    <td align="right">1.10</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
    <td align="right">1.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.32</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="right">1.27</td>
    <td align="center">10</td>
    <td align="right">1.26</td>
    <td align="right">1.31</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
    <td align="center">11</td>
    <td align="right">1.10</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.30</td>
    <td align="right">1.27</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
    <td align="center">12</td>
    <td align="right">1.25</td>
    <td align="right">1.32</td>
    <td align="right">1.30</td>
    <td align="right">1.31</td>
    <td align="center">15</td>
    <td align="right">1.05</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.06</td>
    <td align="right">0.68</td>
    <td align="right">2.05</td>
    <td align="right">1.30</td>
    <td align="center">4</td>
    <td align="right">1.51</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
    <td align="center">5</td>
    <td align="right">1.39</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">2.28</td>
    <td align="right">1.25</td>
    <td align="center">5</td>
    <td align="right">1.99</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">6</td>
    <td align="right">1.81</td>
    <td align="right">1.67</td>
    <td align="right">1.63</td>
    <td align="right">1.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.96</td>
    <td align="right">2.36</td>
    <td align="right">2.59</td>
    <td align="right">1.51</td>
    <td align="center">6</td>
    <td align="right">4.09</td>
    <td align="right">3.43</td>
    <td align="right">3.41</td>
    <td align="right">3.42</td>
    <td align="center">7</td>
    <td align="right">2.80</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">2.17</td>
    <td align="right">2.57</td>
    <td align="right">2.62</td>
    <td align="right">1.45</td>
    <td align="center">7</td>
    <td align="right">4.57</td>
    <td align="right">4.17</td>
    <td align="right">4.17</td>
    <td align="right">4.16</td>
    <td align="center">8</td>
    <td align="right">2.82</td>
    <td align="right">3.07</td>
    <td align="right">3.08</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.58</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="center">5</td>
    <td align="right">0.98</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="center">5</td>
    <td align="right">1.23</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">2.02</td>
    <td align="right">1.92</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="center">8</td>
    <td align="right">1.14</td>
    <td align="right">1.62</td>
    <td align="right">1.66</td>
    <td align="right">1.63</td>
    <td align="center">8</td>
    <td align="right">2.45</td>
    <td align="right">2.17</td>
    <td align="right">2.13</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">3.43</td>
    <td align="right">3.12</td>
    <td align="right">3.08</td>
    <td align="right">3.11</td>
    <td align="center">11</td>
    <td align="right">2.40</td>
    <td align="right">3.39</td>
    <td align="right">3.32</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">1.35</td>
    <td align="right">1.18</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">3.37</td>
    <td align="right">2.89</td>
    <td align="right">2.97</td>
    <td align="right">3.01</td>
    <td align="center">14</td>
    <td align="right">2.38</td>
    <td align="right">2.27</td>
    <td align="right">2.44</td>
    <td align="right">2.25</td>
    <td align="center">13</td>
    <td align="right">1.26</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.20</td>
    <td align="right">0.88</td>
    <td align="right">0.87</td>
    <td align="right">0.87</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">5</td>
    <td align="right">1.14</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
    <td align="right">0.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.69</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="right">1.31</td>
    <td align="center">8</td>
    <td align="right">2.17</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="right">1.71</td>
    <td align="center">8</td>
    <td align="right">1.37</td>
    <td align="right">1.39</td>
    <td align="right">1.37</td>
    <td align="right">1.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.39</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">2.60</td>
    <td align="right">2.58</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="center">11</td>
    <td align="right">2.62</td>
    <td align="right">2.14</td>
    <td align="right">1.93</td>
    <td align="right">1.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.33</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="center">13</td>
    <td align="right">1.83</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.55</td>
    <td align="center">14</td>
    <td align="right">2.40</td>
    <td align="right">1.45</td>
    <td align="right">1.63</td>
    <td align="right">1.47</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.44</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="right">1.38</td>
    <td align="center">6</td>
    <td align="right">1.08</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="center">7</td>
    <td align="right">1.32</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.75</td>
    <td align="right">1.78</td>
    <td align="right">1.78</td>
    <td align="right">1.77</td>
    <td align="center">7</td>
    <td align="right">1.40</td>
    <td align="right">1.57</td>
    <td align="right">1.55</td>
    <td align="right">1.54</td>
    <td align="center">10</td>
    <td align="right">1.19</td>
    <td align="right">1.10</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">2.83</td>
    <td align="right">2.70</td>
    <td align="right">2.62</td>
    <td align="right">2.68</td>
    <td align="center">10</td>
    <td align="right">2.13</td>
    <td align="right">2.13</td>
    <td align="right">2.14</td>
    <td align="right">2.15</td>
    <td align="center">11</td>
    <td align="right">1.50</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
    <td align="right">1.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">3.07</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="right">3.24</td>
    <td align="center">12</td>
    <td align="right">1.94</td>
    <td align="right">1.92</td>
    <td align="right">1.92</td>
    <td align="right">1.93</td>
    <td align="center">15</td>
    <td align="right">1.35</td>
    <td align="right">1.45</td>
    <td align="right">1.44</td>
    <td align="right">1.45</td>
  </tr>
</table>

<!--vs-x64/bulk_comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.25</td>
    <td align="right">0.56</td>
    <td align="right">1.13</td>
    <td align="right">0.69</td>
    <td align="center">4</td>
    <td align="right">1.25</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.06</td>
    <td align="center">5</td>
    <td align="right">1.21</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="right">1.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.06</td>
    <td align="right">0.59</td>
    <td align="right">1.15</td>
    <td align="right">0.61</td>
    <td align="center">5</td>
    <td align="right">1.31</td>
    <td align="right">1.56</td>
    <td align="right">1.54</td>
    <td align="right">1.57</td>
    <td align="center">6</td>
    <td align="right">1.22</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.09</td>
    <td align="right">0.61</td>
    <td align="right">1.15</td>
    <td align="right">0.55</td>
    <td align="center">6</td>
    <td align="right">1.19</td>
    <td align="right">0.92</td>
    <td align="right">0.89</td>
    <td align="right">0.93</td>
    <td align="center">7</td>
    <td align="right">1.22</td>
    <td align="right">1.15</td>
    <td align="right">1.14</td>
    <td align="right">1.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="right">1.33</td>
    <td align="right">0.58</td>
    <td align="center">7</td>
    <td align="right">1.25</td>
    <td align="right">0.89</td>
    <td align="right">0.88</td>
    <td align="right">0.89</td>
    <td align="center">8</td>
    <td align="right">1.16</td>
    <td align="right">1.13</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">0.75</td>
    <td align="right">1.14</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">0.77</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">1.62</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.06</td>
    <td align="right">1.26</td>
    <td align="right">1.28</td>
    <td align="right">1.27</td>
    <td align="center">8</td>
    <td align="right">0.94</td>
    <td align="right">1.11</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
    <td align="center">8</td>
    <td align="right">1.80</td>
    <td align="right">1.24</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.11</td>
    <td align="right">1.16</td>
    <td align="right">1.11</td>
    <td align="right">1.09</td>
    <td align="center">11</td>
    <td align="right">1.04</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="center">11</td>
    <td align="right">0.85</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.13</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.15</td>
    <td align="center">14</td>
    <td align="right">1.20</td>
    <td align="right">1.09</td>
    <td align="right">1.10</td>
    <td align="right">1.09</td>
    <td align="center">13</td>
    <td align="right">0.85</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.01</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="right">1.26</td>
    <td align="center">5</td>
    <td align="right">1.03</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="right">1.36</td>
    <td align="center">5</td>
    <td align="right">1.08</td>
    <td align="right">1.38</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.99</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
    <td align="center">8</td>
    <td align="right">1.91</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
    <td align="center">8</td>
    <td align="right">1.98</td>
    <td align="right">1.38</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.87</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="center">11</td>
    <td align="right">0.89</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="center">11</td>
    <td align="right">0.90</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.86</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="center">13</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
    <td align="right">0.91</td>
    <td align="center">14</td>
    <td align="right">0.88</td>
    <td align="right">0.92</td>
    <td align="right">0.92</td>
    <td align="right">0.93</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.16</td>
    <td align="right">1.12</td>
    <td align="right">1.11</td>
    <td align="right">1.12</td>
    <td align="center">6</td>
    <td align="right">1.08</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="right">0.88</td>
    <td align="center">7</td>
    <td align="right">1.10</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="right">1.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.23</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="center">7</td>
    <td align="right">1.24</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="center">10</td>
    <td align="right">1.13</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.31</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.09</td>
    <td align="center">10</td>
    <td align="right">1.26</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="center">11</td>
    <td align="right">1.19</td>
    <td align="right">1.06</td>
    <td align="right">1.05</td>
    <td align="right">1.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.19</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">12</td>
    <td align="right">1.12</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
    <td align="center">15</td>
    <td align="right">1.05</td>
    <td align="right">0.98</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.14</td>
    <td align="right">0.65</td>
    <td align="right">1.23</td>
    <td align="right">0.75</td>
    <td align="center">4</td>
    <td align="right">1.17</td>
    <td align="right">1.11</td>
    <td align="right">1.08</td>
    <td align="right">1.07</td>
    <td align="center">5</td>
    <td align="right">1.11</td>
    <td align="right">1.06</td>
    <td align="right">1.03</td>
    <td align="right">1.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.68</td>
    <td align="right">0.98</td>
    <td align="right">1.42</td>
    <td align="right">0.77</td>
    <td align="center">5</td>
    <td align="right">1.49</td>
    <td align="right">1.63</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="center">6</td>
    <td align="right">1.54</td>
    <td align="right">1.35</td>
    <td align="right">1.40</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.54</td>
    <td align="right">1.65</td>
    <td align="right">1.99</td>
    <td align="right">1.01</td>
    <td align="center">6</td>
    <td align="right">2.04</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="right">1.83</td>
    <td align="center">7</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="right">1.86</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">2.96</td>
    <td align="right">2.19</td>
    <td align="right">2.29</td>
    <td align="right">1.07</td>
    <td align="center">7</td>
    <td align="right">2.26</td>
    <td align="right">2.04</td>
    <td align="right">2.03</td>
    <td align="right">2.08</td>
    <td align="center">8</td>
    <td align="right">2.36</td>
    <td align="right">2.18</td>
    <td align="right">2.19</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">0.81</td>
    <td align="right">1.36</td>
    <td align="right">1.36</td>
    <td align="right">1.37</td>
    <td align="center">5</td>
    <td align="right">0.84</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">5</td>
    <td align="right">1.54</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.17</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="right">1.63</td>
    <td align="center">8</td>
    <td align="right">1.09</td>
    <td align="right">1.57</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
    <td align="center">8</td>
    <td align="right">2.21</td>
    <td align="right">1.66</td>
    <td align="right">1.66</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.35</td>
    <td align="right">1.78</td>
    <td align="right">1.77</td>
    <td align="right">1.70</td>
    <td align="center">11</td>
    <td align="right">1.33</td>
    <td align="right">1.70</td>
    <td align="right">1.75</td>
    <td align="right">1.77</td>
    <td align="center">11</td>
    <td align="right">1.57</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.44</td>
    <td align="right">2.13</td>
    <td align="right">2.14</td>
    <td align="right">2.14</td>
    <td align="center">14</td>
    <td align="right">1.49</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
    <td align="right">2.00</td>
    <td align="center">13</td>
    <td align="right">1.84</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.86</td>
    <td align="right">1.26</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
    <td align="center">5</td>
    <td align="right">1.07</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
    <td align="right">1.39</td>
    <td align="center">5</td>
    <td align="right">1.09</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">2.35</td>
    <td align="right">1.75</td>
    <td align="right">1.74</td>
    <td align="right">1.75</td>
    <td align="center">8</td>
    <td align="right">2.17</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">2.44</td>
    <td align="right">2.00</td>
    <td align="right">2.01</td>
    <td align="right">2.00</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.55</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.56</td>
    <td align="center">11</td>
    <td align="right">1.48</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
    <td align="right">1.55</td>
    <td align="center">11</td>
    <td align="right">1.45</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.82</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="center">13</td>
    <td align="right">1.73</td>
    <td align="right">1.67</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">14</td>
    <td align="right">1.66</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.19</td>
    <td align="center">6</td>
    <td align="right">1.14</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="center">7</td>
    <td align="right">1.18</td>
    <td align="right">1.16</td>
    <td align="right">1.19</td>
    <td align="right">1.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.52</td>
    <td align="right">1.39</td>
    <td align="right">1.32</td>
    <td align="right">1.40</td>
    <td align="center">7</td>
    <td align="right">1.69</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="right">1.37</td>
    <td align="center">10</td>
    <td align="right">1.44</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.99</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.79</td>
    <td align="center">10</td>
    <td align="right">2.18</td>
    <td align="right">1.74</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="center">11</td>
    <td align="right">1.73</td>
    <td align="right">1.77</td>
    <td align="right">1.77</td>
    <td align="right">1.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">2.01</td>
    <td align="right">1.80</td>
    <td align="right">1.83</td>
    <td align="right">1.80</td>
    <td align="center">12</td>
    <td align="right">2.04</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">15</td>
    <td align="right">1.55</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
  </tr>
</table>

<!--gcc-x86/bulk_comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.72</td>
    <td align="right">0.69</td>
    <td align="right">1.52</td>
    <td align="right">0.97</td>
    <td align="center">4</td>
    <td align="right">0.89</td>
    <td align="right">1.18</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="center">5</td>
    <td align="right">0.89</td>
    <td align="right">1.17</td>
    <td align="right">1.17</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.82</td>
    <td align="right">0.60</td>
    <td align="right">1.55</td>
    <td align="right">0.79</td>
    <td align="center">5</td>
    <td align="right">0.92</td>
    <td align="right">1.17</td>
    <td align="right">1.15</td>
    <td align="right">1.16</td>
    <td align="center">6</td>
    <td align="right">0.90</td>
    <td align="right">1.13</td>
    <td align="right">1.12</td>
    <td align="right">1.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.66</td>
    <td align="right">0.60</td>
    <td align="right">1.31</td>
    <td align="right">0.62</td>
    <td align="center">6</td>
    <td align="right">0.97</td>
    <td align="right">1.16</td>
    <td align="right">1.16</td>
    <td align="right">1.15</td>
    <td align="center">7</td>
    <td align="right">0.91</td>
    <td align="right">1.17</td>
    <td align="right">1.24</td>
    <td align="right">1.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.87</td>
    <td align="right">0.56</td>
    <td align="right">1.28</td>
    <td align="right">0.52</td>
    <td align="center">7</td>
    <td align="right">0.95</td>
    <td align="right">1.19</td>
    <td align="right">1.21</td>
    <td align="right">1.20</td>
    <td align="center">8</td>
    <td align="right">0.88</td>
    <td align="right">1.20</td>
    <td align="right">1.21</td>
    <td align="right">1.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.01</td>
    <td align="right">1.25</td>
    <td align="right">1.23</td>
    <td align="right">1.24</td>
    <td align="center">5</td>
    <td align="right">0.95</td>
    <td align="right">1.30</td>
    <td align="right">1.31</td>
    <td align="right">1.29</td>
    <td align="center">5</td>
    <td align="right">0.94</td>
    <td align="right">1.14</td>
    <td align="right">1.13</td>
    <td align="right">1.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.93</td>
    <td align="right">1.37</td>
    <td align="right">1.36</td>
    <td align="right">1.37</td>
    <td align="center">8</td>
    <td align="right">0.77</td>
    <td align="right">1.31</td>
    <td align="right">1.28</td>
    <td align="right">1.33</td>
    <td align="center">8</td>
    <td align="right">0.91</td>
    <td align="right">1.24</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.02</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">0.92</td>
    <td align="right">1.22</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">11</td>
    <td align="right">0.96</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.13</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
    <td align="center">14</td>
    <td align="right">0.91</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
    <td align="center">13</td>
    <td align="right">0.96</td>
    <td align="right">1.21</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">0.82</td>
    <td align="right">1.15</td>
    <td align="right">1.12</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">0.88</td>
    <td align="right">1.36</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
    <td align="center">5</td>
    <td align="right">0.78</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
    <td align="right">1.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.82</td>
    <td align="right">1.16</td>
    <td align="right">1.18</td>
    <td align="right">1.19</td>
    <td align="center">8</td>
    <td align="right">0.92</td>
    <td align="right">1.23</td>
    <td align="right">1.27</td>
    <td align="right">1.26</td>
    <td align="center">8</td>
    <td align="right">0.90</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
    <td align="right">1.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.98</td>
    <td align="right">1.17</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">0.99</td>
    <td align="right">1.20</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">11</td>
    <td align="right">0.99</td>
    <td align="right">1.24</td>
    <td align="right">1.25</td>
    <td align="right">1.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.99</td>
    <td align="right">1.17</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="center">13</td>
    <td align="right">0.99</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="center">14</td>
    <td align="right">1.00</td>
    <td align="right">1.16</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.16</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
    <td align="center">6</td>
    <td align="right">0.99</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="center">7</td>
    <td align="right">1.08</td>
    <td align="right">1.20</td>
    <td align="right">1.21</td>
    <td align="right">1.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.17</td>
    <td align="right">1.23</td>
    <td align="right">1.24</td>
    <td align="right">1.22</td>
    <td align="center">7</td>
    <td align="right">1.01</td>
    <td align="right">1.36</td>
    <td align="right">1.43</td>
    <td align="right">1.35</td>
    <td align="center">10</td>
    <td align="right">1.03</td>
    <td align="right">1.12</td>
    <td align="right">1.15</td>
    <td align="right">1.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">2.69</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="right">1.19</td>
    <td align="center">10</td>
    <td align="right">1.12</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="right">1.31</td>
    <td align="center">11</td>
    <td align="right">1.04</td>
    <td align="right">1.17</td>
    <td align="right">1.15</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="right">1.21</td>
    <td align="center">12</td>
    <td align="right">1.17</td>
    <td align="right">1.35</td>
    <td align="right">1.38</td>
    <td align="right">1.38</td>
    <td align="center">15</td>
    <td align="right">0.76</td>
    <td align="right">1.25</td>
    <td align="right">1.22</td>
    <td align="right">1.24</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">0.81</td>
    <td align="right">0.76</td>
    <td align="right">1.60</td>
    <td align="right">0.99</td>
    <td align="center">4</td>
    <td align="right">1.01</td>
    <td align="right">1.31</td>
    <td align="right">1.27</td>
    <td align="right">1.33</td>
    <td align="center">5</td>
    <td align="right">1.00</td>
    <td align="right">1.25</td>
    <td align="right">1.24</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.48</td>
    <td align="right">1.14</td>
    <td align="right">1.82</td>
    <td align="right">1.02</td>
    <td align="center">5</td>
    <td align="right">1.45</td>
    <td align="right">1.73</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="center">6</td>
    <td align="right">1.67</td>
    <td align="right">1.80</td>
    <td align="right">1.76</td>
    <td align="right">1.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.88</td>
    <td align="right">1.71</td>
    <td align="right">2.11</td>
    <td align="right">1.11</td>
    <td align="center">6</td>
    <td align="right">2.59</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.54</td>
    <td align="center">7</td>
    <td align="right">2.20</td>
    <td align="right">2.69</td>
    <td align="right">2.52</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">2.79</td>
    <td align="right">2.19</td>
    <td align="right">2.45</td>
    <td align="right">1.19</td>
    <td align="center">7</td>
    <td align="right">2.66</td>
    <td align="right">3.09</td>
    <td align="right">3.23</td>
    <td align="right">3.06</td>
    <td align="center">8</td>
    <td align="right">2.67</td>
    <td align="right">3.35</td>
    <td align="right">3.36</td>
    <td align="right">3.30</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.17</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="right">1.34</td>
    <td align="center">5</td>
    <td align="right">1.03</td>
    <td align="right">1.37</td>
    <td align="right">1.36</td>
    <td align="right">1.36</td>
    <td align="center">5</td>
    <td align="right">1.06</td>
    <td align="right">1.26</td>
    <td align="right">1.32</td>
    <td align="right">1.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.71</td>
    <td align="right">2.21</td>
    <td align="right">2.30</td>
    <td align="right">2.30</td>
    <td align="center">8</td>
    <td align="right">1.71</td>
    <td align="right">2.37</td>
    <td align="right">2.43</td>
    <td align="right">2.38</td>
    <td align="center">8</td>
    <td align="right">1.75</td>
    <td align="right">2.18</td>
    <td align="right">2.15</td>
    <td align="right">2.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.08</td>
    <td align="right">2.48</td>
    <td align="right">2.55</td>
    <td align="right">2.49</td>
    <td align="center">11</td>
    <td align="right">1.99</td>
    <td align="right">2.40</td>
    <td align="right">2.37</td>
    <td align="right">2.40</td>
    <td align="center">11</td>
    <td align="right">2.47</td>
    <td align="right">3.04</td>
    <td align="right">3.02</td>
    <td align="right">3.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.06</td>
    <td align="right">2.74</td>
    <td align="right">2.65</td>
    <td align="right">2.68</td>
    <td align="center">14</td>
    <td align="right">2.04</td>
    <td align="right">2.71</td>
    <td align="right">2.71</td>
    <td align="right">2.71</td>
    <td align="center">13</td>
    <td align="right">2.92</td>
    <td align="right">3.66</td>
    <td align="right">3.63</td>
    <td align="right">3.63</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">0.98</td>
    <td align="right">1.35</td>
    <td align="right">1.33</td>
    <td align="right">1.34</td>
    <td align="center">5</td>
    <td align="right">1.00</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.57</td>
    <td align="center">5</td>
    <td align="right">0.85</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.58</td>
    <td align="right">2.07</td>
    <td align="right">2.06</td>
    <td align="right">2.05</td>
    <td align="center">8</td>
    <td align="right">1.66</td>
    <td align="right">2.00</td>
    <td align="right">2.10</td>
    <td align="right">2.09</td>
    <td align="center">8</td>
    <td align="right">1.61</td>
    <td align="right">2.37</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.53</td>
    <td align="right">3.10</td>
    <td align="right">3.15</td>
    <td align="right">3.10</td>
    <td align="center">11</td>
    <td align="right">2.09</td>
    <td align="right">2.49</td>
    <td align="right">2.44</td>
    <td align="right">2.47</td>
    <td align="center">11</td>
    <td align="right">2.07</td>
    <td align="right">2.57</td>
    <td align="right">2.59</td>
    <td align="right">2.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.99</td>
    <td align="right">3.75</td>
    <td align="right">3.73</td>
    <td align="right">3.74</td>
    <td align="center">13</td>
    <td align="right">2.08</td>
    <td align="right">2.61</td>
    <td align="right">2.65</td>
    <td align="right">2.61</td>
    <td align="center">14</td>
    <td align="right">2.06</td>
    <td align="right">2.66</td>
    <td align="right">2.63</td>
    <td align="right">2.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.32</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">1.12</td>
    <td align="right">1.67</td>
    <td align="right">1.60</td>
    <td align="right">1.68</td>
    <td align="center">7</td>
    <td align="right">1.13</td>
    <td align="right">1.25</td>
    <td align="right">1.25</td>
    <td align="right">1.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.57</td>
    <td align="right">1.62</td>
    <td align="right">1.65</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">1.55</td>
    <td align="right">2.06</td>
    <td align="right">2.00</td>
    <td align="right">2.06</td>
    <td align="center">10</td>
    <td align="right">1.42</td>
    <td align="right">1.63</td>
    <td align="right">1.66</td>
    <td align="right">1.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">2.89</td>
    <td align="right">2.34</td>
    <td align="right">2.36</td>
    <td align="right">2.34</td>
    <td align="center">10</td>
    <td align="right">2.32</td>
    <td align="right">2.66</td>
    <td align="right">2.63</td>
    <td align="right">2.62</td>
    <td align="center">11</td>
    <td align="right">1.66</td>
    <td align="right">1.65</td>
    <td align="right">1.65</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">2.51</td>
    <td align="right">2.69</td>
    <td align="right">2.70</td>
    <td align="right">2.68</td>
    <td align="center">12</td>
    <td align="right">2.84</td>
    <td align="right">3.09</td>
    <td align="right">3.13</td>
    <td align="right">3.13</td>
    <td align="center">15</td>
    <td align="right">1.40</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
  </tr>
</table>

<!--clang-x86/bulk_comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/bulk_comparison_table.cpp.txt-->

#### `N` = 1M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.13</td>
    <td align="right">0.71</td>
    <td align="right">0.81</td>
    <td align="right">0.63</td>
    <td align="center">4</td>
    <td align="right">1.05</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="center">5</td>
    <td align="right">1.08</td>
    <td align="right">1.08</td>
    <td align="right">1.03</td>
    <td align="right">0.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.15</td>
    <td align="right">0.71</td>
    <td align="right">0.82</td>
    <td align="right">0.53</td>
    <td align="center">5</td>
    <td align="right">1.05</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="right">0.93</td>
    <td align="center">6</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">1.09</td>
    <td align="right">0.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.18</td>
    <td align="right">0.73</td>
    <td align="right">0.83</td>
    <td align="right">0.50</td>
    <td align="center">6</td>
    <td align="right">1.05</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="right">0.92</td>
    <td align="center">7</td>
    <td align="right">1.09</td>
    <td align="right">1.11</td>
    <td align="right">1.11</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">1.21</td>
    <td align="right">0.75</td>
    <td align="right">0.82</td>
    <td align="right">0.44</td>
    <td align="center">7</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.01</td>
    <td align="right">0.93</td>
    <td align="center">8</td>
    <td align="right">1.09</td>
    <td align="right">1.12</td>
    <td align="right">1.10</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.09</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.14</td>
    <td align="center">5</td>
    <td align="right">1.15</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">1.17</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.17</td>
    <td align="right">1.00</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="center">8</td>
    <td align="right">1.19</td>
    <td align="right">0.99</td>
    <td align="right">0.98</td>
    <td align="right">0.97</td>
    <td align="center">8</td>
    <td align="right">1.19</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.07</td>
    <td align="right">1.04</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">11</td>
    <td align="right">1.16</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
    <td align="center">11</td>
    <td align="right">1.25</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.08</td>
    <td align="right">1.00</td>
    <td align="right">1.03</td>
    <td align="right">1.01</td>
    <td align="center">14</td>
    <td align="right">1.16</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
    <td align="center">13</td>
    <td align="right">1.25</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">1.84</td>
    <td align="right">1.85</td>
    <td align="right">1.82</td>
    <td align="center">5</td>
    <td align="right">1.27</td>
    <td align="right">1.89</td>
    <td align="right">1.89</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">1.31</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.19</td>
    <td align="right">2.44</td>
    <td align="right">2.43</td>
    <td align="right">2.43</td>
    <td align="center">8</td>
    <td align="right">1.31</td>
    <td align="right">2.47</td>
    <td align="right">2.46</td>
    <td align="right">2.47</td>
    <td align="center">8</td>
    <td align="right">1.36</td>
    <td align="right">2.40</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.29</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="center">11</td>
    <td align="right">1.02</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="right">1.54</td>
    <td align="center">11</td>
    <td align="right">1.02</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.29</td>
    <td align="right">1.54</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="center">13</td>
    <td align="right">1.02</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="right">1.53</td>
    <td align="center">14</td>
    <td align="right">1.04</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.12</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">6</td>
    <td align="right">1.16</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="center">7</td>
    <td align="right">1.02</td>
    <td align="right">0.99</td>
    <td align="right">1.01</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.09</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.01</td>
    <td align="center">7</td>
    <td align="right">1.15</td>
    <td align="right">1.08</td>
    <td align="right">1.06</td>
    <td align="right">1.06</td>
    <td align="center">10</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.09</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">10</td>
    <td align="right">1.15</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="right">1.03</td>
    <td align="center">11</td>
    <td align="right">1.00</td>
    <td align="right">0.98</td>
    <td align="right">0.99</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.06</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">12</td>
    <td align="right">1.13</td>
    <td align="right">0.99</td>
    <td align="right">1.02</td>
    <td align="right">1.00</td>
    <td align="center">15</td>
    <td align="right">0.96</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
    <td align="right">0.98</td>
  </tr>
</table>

#### `N` = 10M elements
<table class="bordered_table" style="font-size: 85%;">
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,K></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">1.22</td>
    <td align="right">0.72</td>
    <td align="right">0.82</td>
    <td align="right">0.65</td>
    <td align="center">4</td>
    <td align="right">1.05</td>
    <td align="right">0.98</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="center">5</td>
    <td align="right">1.16</td>
    <td align="right">1.14</td>
    <td align="right">1.09</td>
    <td align="right">1.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">1.43</td>
    <td align="right">0.93</td>
    <td align="right">0.93</td>
    <td align="right">0.63</td>
    <td align="center">5</td>
    <td align="right">1.12</td>
    <td align="right">1.06</td>
    <td align="right">1.08</td>
    <td align="right">0.98</td>
    <td align="center">6</td>
    <td align="right">1.21</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="right">1.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.42</td>
    <td align="right">1.48</td>
    <td align="right">1.26</td>
    <td align="right">0.82</td>
    <td align="center">6</td>
    <td align="right">1.55</td>
    <td align="right">1.49</td>
    <td align="right">1.48</td>
    <td align="right">1.33</td>
    <td align="center">7</td>
    <td align="right">1.77</td>
    <td align="right">1.80</td>
    <td align="right">1.75</td>
    <td align="right">1.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">3.24</td>
    <td align="right">1.93</td>
    <td align="right">1.55</td>
    <td align="right">0.92</td>
    <td align="center">7</td>
    <td align="right">1.74</td>
    <td align="right">1.70</td>
    <td align="right">1.68</td>
    <td align="right">1.52</td>
    <td align="center">8</td>
    <td align="right">2.13</td>
    <td align="right">2.14</td>
    <td align="right">2.12</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.16</td>
    <td align="right">1.04</td>
    <td align="right">1.03</td>
    <td align="right">1.14</td>
    <td align="center">5</td>
    <td align="right">1.21</td>
    <td align="right">1.03</td>
    <td align="right">1.02</td>
    <td align="right">1.03</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">1.94</td>
    <td align="right">1.94</td>
    <td align="right">1.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.32</td>
    <td align="right">1.03</td>
    <td align="right">1.05</td>
    <td align="right">1.04</td>
    <td align="center">8</td>
    <td align="right">1.37</td>
    <td align="right">1.03</td>
    <td align="right">1.01</td>
    <td align="right">1.02</td>
    <td align="center">8</td>
    <td align="right">1.32</td>
    <td align="right">2.73</td>
    <td align="right">2.72</td>
    <td align="right">2.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">1.60</td>
    <td align="right">1.20</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">11</td>
    <td align="right">1.74</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">11</td>
    <td align="right">2.10</td>
    <td align="right">2.34</td>
    <td align="right">2.32</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">1.94</td>
    <td align="right">1.28</td>
    <td align="right">1.30</td>
    <td align="right">1.29</td>
    <td align="center">14</td>
    <td align="right">2.07</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="right">1.30</td>
    <td align="center">13</td>
    <td align="right">2.65</td>
    <td align="right">2.74</td>
    <td align="right">2.74</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.19</td>
    <td align="right">1.95</td>
    <td align="right">1.95</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">1.28</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="right">1.95</td>
    <td align="center">5</td>
    <td align="right">1.32</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
    <td align="right">1.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">1.32</td>
    <td align="right">2.63</td>
    <td align="right">2.64</td>
    <td align="right">2.60</td>
    <td align="center">8</td>
    <td align="right">1.44</td>
    <td align="right">2.66</td>
    <td align="right">2.64</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">1.48</td>
    <td align="right">2.75</td>
    <td align="right">2.71</td>
    <td align="right">2.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">2.27</td>
    <td align="right">2.29</td>
    <td align="right">2.27</td>
    <td align="right">2.29</td>
    <td align="center">11</td>
    <td align="right">1.66</td>
    <td align="right">2.24</td>
    <td align="right">2.23</td>
    <td align="right">2.24</td>
    <td align="center">11</td>
    <td align="right">1.64</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">2.75</td>
    <td align="right">2.73</td>
    <td align="right">2.73</td>
    <td align="right">2.73</td>
    <td align="center">13</td>
    <td align="right">1.94</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="right">2.57</td>
    <td align="center">14</td>
    <td align="right">1.94</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">1.18</td>
    <td align="right">1.00</td>
    <td align="right">1.01</td>
    <td align="right">1.01</td>
    <td align="center">6</td>
    <td align="right">1.24</td>
    <td align="right">1.02</td>
    <td align="right">1.02</td>
    <td align="right">1.04</td>
    <td align="center">7</td>
    <td align="right">1.07</td>
    <td align="right">0.99</td>
    <td align="right">1.00</td>
    <td align="right">1.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">1.19</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="right">1.04</td>
    <td align="center">7</td>
    <td align="right">1.30</td>
    <td align="right">1.19</td>
    <td align="right">1.18</td>
    <td align="right">1.17</td>
    <td align="center">10</td>
    <td align="right">1.09</td>
    <td align="right">1.02</td>
    <td align="right">1.00</td>
    <td align="right">0.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">1.56</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="right">1.13</td>
    <td align="center">10</td>
    <td align="right">1.74</td>
    <td align="right">1.35</td>
    <td align="right">1.36</td>
    <td align="right">1.35</td>
    <td align="center">11</td>
    <td align="right">1.55</td>
    <td align="right">1.19</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">1.62</td>
    <td align="right">1.22</td>
    <td align="right">1.21</td>
    <td align="right">1.21</td>
    <td align="center">12</td>
    <td align="right">1.89</td>
    <td align="right">1.37</td>
    <td align="right">1.40</td>
    <td align="right">1.38</td>
    <td align="center">15</td>
    <td align="right">1.43</td>
    <td align="right">1.21</td>
    <td align="right">1.20</td>
    <td align="right">1.20</td>
  </tr>
</table>

<!--vs-x86/bulk_comparison_table.cpp.txt-->
