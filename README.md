# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.62</td>
    <td align="right">5.62</td>
    <td align="right">4.11</td>
    <td align="right">12.48</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.05</td>
    <td align="right">12.11</td>
    <td align="right">18.12</td>
    <td align="right">16.92</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">5.12</td>
    <td align="right">5.11</td>
    <td align="right">5.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.54</td>
    <td align="right">17.87</td>
    <td align="right">19.20</td>
    <td align="right">20.63</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.98</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.34</td>
    <td align="right">21.52</td>
    <td align="right">18.12</td>
    <td align="right">23.16</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.63</td>
    <td align="right">5.64</td>
    <td align="right">5.62</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.24</td>
    <td align="right">27.73</td>
    <td align="right">18.51</td>
    <td align="right">27.69</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.38</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.00</td>
    <td align="right">13.22</td>
    <td align="right">13.25</td>
    <td align="right">13.22</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.01</td>
    <td align="right">4.62</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">5.11</td>
    <td align="right">5.11</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.57</td>
    <td align="right">20.16</td>
    <td align="right">20.07</td>
    <td align="right">20.11</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="right">5.17</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
    <td align="right">5.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.38</td>
    <td align="right">24.41</td>
    <td align="right">24.35</td>
    <td align="right">24.37</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.01</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="right">5.63</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.54</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
    <td align="right">6.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.17</td>
    <td align="right">29.04</td>
    <td align="right">29.26</td>
    <td align="right">29.30</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.98</td>
    <td align="right">5.97</td>
    <td align="right">5.97</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.81</td>
    <td align="right">6.30</td>
    <td align="right">6.29</td>
    <td align="right">6.30</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.01</td>
    <td align="right">5.81</td>
    <td align="right">14.09</td>
    <td align="right">11.73</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.51</td>
    <td align="right">7.62</td>
    <td align="right">14.80</td>
    <td align="right">13.23</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.26</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.87</td>
    <td align="right">8.47</td>
    <td align="right">14.79</td>
    <td align="right">13.67</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.66</td>
    <td align="right">17.89</td>
    <td align="right">15.28</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">2.74</td>
    <td align="right">2.74</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.14</td>
    <td align="right">12.37</td>
    <td align="right">16.04</td>
    <td align="right">17.52</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.11</td>
    <td align="right">13.00</td>
    <td align="right">17.62</td>
    <td align="right">17.84</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.78</td>
    <td align="right">5.86</td>
    <td align="right">4.15</td>
    <td align="right">14.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.45</td>
    <td align="right">13.60</td>
    <td align="right">15.46</td>
    <td align="right">18.25</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.62</td>
    <td align="right">14.85</td>
    <td align="right">18.65</td>
    <td align="right">19.45</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.84</td>
    <td align="right">5.90</td>
    <td align="right">4.15</td>
    <td align="right">14.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.66</td>
    <td align="right">5.65</td>
    <td align="right">5.66</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.51</td>
    <td align="right">6.96</td>
    <td align="right">6.96</td>
    <td align="right">6.98</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.23</td>
    <td align="right">2.95</td>
    <td align="right">2.94</td>
    <td align="right">2.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.87</td>
    <td align="right">9.27</td>
    <td align="right">9.26</td>
    <td align="right">9.27</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.09</td>
    <td align="right">9.70</td>
    <td align="right">9.70</td>
    <td align="right">9.67</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.70</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
    <td align="right">2.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.10</td>
    <td align="right">11.75</td>
    <td align="right">11.76</td>
    <td align="right">11.79</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.13</td>
    <td align="right">13.70</td>
    <td align="right">13.65</td>
    <td align="right">13.68</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.78</td>
    <td align="right">5.84</td>
    <td align="right">5.82</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.40</td>
    <td align="right">12.74</td>
    <td align="right">12.74</td>
    <td align="right">12.74</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.63</td>
    <td align="right">15.13</td>
    <td align="right">15.74</td>
    <td align="right">15.18</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.83</td>
    <td align="right">5.87</td>
    <td align="right">5.86</td>
    <td align="right">5.88</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.18</td>
    <td align="right">2.78</td>
    <td align="right">2.78</td>
    <td align="right">2.79</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.61</td>
    <td align="right">4.78</td>
    <td align="right">4.78</td>
    <td align="right">4.78</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.79</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.31</td>
    <td align="right">2.82</td>
    <td align="right">2.82</td>
    <td align="right">2.84</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.80</td>
    <td align="right">4.71</td>
    <td align="right">4.72</td>
    <td align="right">4.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.56</td>
    <td align="right">5.66</td>
    <td align="right">3.93</td>
    <td align="right">14.34</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.57</td>
    <td align="right">8.18</td>
    <td align="right">6.07</td>
    <td align="right">17.85</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.71</td>
    <td align="right">7.95</td>
    <td align="right">6.02</td>
    <td align="right">17.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.60</td>
    <td align="right">5.68</td>
    <td align="right">3.88</td>
    <td align="right">15.29</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.50</td>
    <td align="right">9.43</td>
    <td align="right">6.28</td>
    <td align="right">18.66</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.66</td>
    <td align="right">9.11</td>
    <td align="right">6.13</td>
    <td align="right">18.33</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.19</td>
    <td align="right">2.77</td>
    <td align="right">2.77</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.62</td>
    <td align="right">4.57</td>
    <td align="right">4.57</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.40</td>
    <td align="right">4.40</td>
    <td align="right">4.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.31</td>
    <td align="right">2.84</td>
    <td align="right">2.86</td>
    <td align="right">2.85</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.80</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="right">5.64</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.60</td>
    <td align="right">7.80</td>
    <td align="right">7.76</td>
    <td align="right">7.85</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.79</td>
    <td align="right">7.69</td>
    <td align="right">7.59</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.51</td>
    <td align="right">8.68</td>
    <td align="right">8.66</td>
    <td align="right">8.67</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.61</td>
    <td align="right">8.41</td>
    <td align="right">8.41</td>
    <td align="right">8.41</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.42</td>
    <td align="right">7.33</td>
    <td align="right">14.46</td>
    <td align="right">12.68</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">8.81</td>
    <td align="right">18.89</td>
    <td align="right">15.78</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.51</td>
    <td align="right">11.88</td>
    <td align="right">19.35</td>
    <td align="right">16.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.41</td>
    <td align="right">14.43</td>
    <td align="right">15.81</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">10.54</td>
    <td align="right">16.19</td>
    <td align="right">17.17</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.14</td>
    <td align="right">14.39</td>
    <td align="right">20.63</td>
    <td align="right">19.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.66</td>
    <td align="right">11.92</td>
    <td align="right">14.07</td>
    <td align="right">16.77</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.94</td>
    <td align="right">12.94</td>
    <td align="right">17.36</td>
    <td align="right">19.70</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.44</td>
    <td align="right">15.60</td>
    <td align="right">18.88</td>
    <td align="right">19.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.85</td>
    <td align="right">14.36</td>
    <td align="right">14.78</td>
    <td align="right">18.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.61</td>
    <td align="right">15.15</td>
    <td align="right">16.91</td>
    <td align="right">20.08</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.71</td>
    <td align="right">20.53</td>
    <td align="right">20.87</td>
    <td align="right">22.91</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.41</td>
    <td align="right">6.91</td>
    <td align="right">6.91</td>
    <td align="right">6.92</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.39</td>
    <td align="right">8.39</td>
    <td align="right">8.39</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.41</td>
    <td align="right">11.34</td>
    <td align="right">11.37</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.75</td>
    <td align="right">9.90</td>
    <td align="right">9.92</td>
    <td align="right">9.91</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">10.92</td>
    <td align="right">10.92</td>
    <td align="right">10.91</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.99</td>
    <td align="right">14.26</td>
    <td align="right">13.90</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.64</td>
    <td align="right">11.04</td>
    <td align="right">11.04</td>
    <td align="right">11.04</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.97</td>
    <td align="right">13.13</td>
    <td align="right">13.13</td>
    <td align="right">13.13</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.27</td>
    <td align="right">16.25</td>
    <td align="right">16.24</td>
    <td align="right">16.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.83</td>
    <td align="right">14.18</td>
    <td align="right">14.18</td>
    <td align="right">14.18</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.62</td>
    <td align="right">15.98</td>
    <td align="right">15.98</td>
    <td align="right">16.00</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.79</td>
    <td align="right">20.94</td>
    <td align="right">20.95</td>
    <td align="right">21.03</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.44</td>
    <td align="right">23.49</td>
    <td align="right">14.31</td>
    <td align="right">31.74</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.29</td>
    <td align="right">17.08</td>
    <td align="right">21.08</td>
    <td align="right">20.58</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.42</td>
    <td align="right">6.10</td>
    <td align="right">6.11</td>
    <td align="right">6.12</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.58</td>
    <td align="right">6.29</td>
    <td align="right">6.33</td>
    <td align="right">6.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">47.38</td>
    <td align="right">51.41</td>
    <td align="right">27.45</td>
    <td align="right">40.98</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.70</td>
    <td align="right">11.67</td>
    <td align="right">11.76</td>
    <td align="right">11.62</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.71</td>
    <td align="right">12.70</td>
    <td align="right">12.69</td>
    <td align="right">12.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.63</td>
    <td align="right">93.16</td>
    <td align="right">33.66</td>
    <td align="right">65.99</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.69</td>
    <td align="right">18.38</td>
    <td align="right">18.37</td>
    <td align="right">18.37</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.88</td>
    <td align="right">18.98</td>
    <td align="right">18.98</td>
    <td align="right">19.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">129.79</td>
    <td align="right">142.36</td>
    <td align="right">41.00</td>
    <td align="right">96.06</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.85</td>
    <td align="right">21.95</td>
    <td align="right">21.96</td>
    <td align="right">21.95</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.87</td>
    <td align="right">25.17</td>
    <td align="right">25.22</td>
    <td align="right">25.19</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.44</td>
    <td align="right">17.12</td>
    <td align="right">17.15</td>
    <td align="right">17.83</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.04</td>
    <td align="right">5.71</td>
    <td align="right">5.71</td>
    <td align="right">5.69</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.18</td>
    <td align="right">5.78</td>
    <td align="right">5.79</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">45.95</td>
    <td align="right">49.87</td>
    <td align="right">49.93</td>
    <td align="right">49.86</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.96</td>
    <td align="right">11.95</td>
    <td align="right">11.98</td>
    <td align="right">11.96</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.86</td>
    <td align="right">12.88</td>
    <td align="right">12.84</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">86.56</td>
    <td align="right">88.89</td>
    <td align="right">87.97</td>
    <td align="right">88.11</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.65</td>
    <td align="right">18.18</td>
    <td align="right">18.19</td>
    <td align="right">18.17</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.81</td>
    <td align="right">18.90</td>
    <td align="right">18.88</td>
    <td align="right">18.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.16</td>
    <td align="right">132.22</td>
    <td align="right">138.75</td>
    <td align="right">138.70</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.86</td>
    <td align="right">21.97</td>
    <td align="right">21.97</td>
    <td align="right">21.98</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.92</td>
    <td align="right">25.22</td>
    <td align="right">25.23</td>
    <td align="right">25.25</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.44</td>
    <td align="right">7.36</td>
    <td align="right">14.94</td>
    <td align="right">13.78</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.33</td>
    <td align="right">8.85</td>
    <td align="right">16.31</td>
    <td align="right">14.95</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.28</td>
    <td align="right">4.04</td>
    <td align="right">4.07</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.02</td>
    <td align="right">15.52</td>
    <td align="right">18.86</td>
    <td align="right">20.15</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.35</td>
    <td align="right">18.68</td>
    <td align="right">23.24</td>
    <td align="right">22.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.79</td>
    <td align="right">8.07</td>
    <td align="right">8.08</td>
    <td align="right">8.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.30</td>
    <td align="right">30.12</td>
    <td align="right">25.64</td>
    <td align="right">30.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.05</td>
    <td align="right">32.48</td>
    <td align="right">29.67</td>
    <td align="right">34.21</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.12</td>
    <td align="right">20.56</td>
    <td align="right">14.87</td>
    <td align="right">24.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.63</td>
    <td align="right">40.11</td>
    <td align="right">26.71</td>
    <td align="right">39.24</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.69</td>
    <td align="right">43.32</td>
    <td align="right">33.57</td>
    <td align="right">44.97</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.22</td>
    <td align="right">23.76</td>
    <td align="right">16.80</td>
    <td align="right">28.54</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.06</td>
    <td align="right">6.50</td>
    <td align="right">6.49</td>
    <td align="right">6.47</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.85</td>
    <td align="right">8.62</td>
    <td align="right">8.62</td>
    <td align="right">8.61</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.38</td>
    <td align="right">4.11</td>
    <td align="right">4.12</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.04</td>
    <td align="right">16.43</td>
    <td align="right">16.40</td>
    <td align="right">16.41</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.94</td>
    <td align="right">20.22</td>
    <td align="right">20.19</td>
    <td align="right">20.21</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.51</td>
    <td align="right">7.75</td>
    <td align="right">7.72</td>
    <td align="right">7.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">28.89</td>
    <td align="right">30.07</td>
    <td align="right">30.09</td>
    <td align="right">30.09</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.42</td>
    <td align="right">35.39</td>
    <td align="right">35.04</td>
    <td align="right">34.94</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.04</td>
    <td align="right">20.75</td>
    <td align="right">20.73</td>
    <td align="right">20.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.47</td>
    <td align="right">39.18</td>
    <td align="right">39.21</td>
    <td align="right">39.18</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.93</td>
    <td align="right">51.94</td>
    <td align="right">51.54</td>
    <td align="right">51.99</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.19</td>
    <td align="right">23.99</td>
    <td align="right">24.01</td>
    <td align="right">24.00</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">5.23</td>
    <td align="right">4.95</td>
    <td align="right">4.92</td>
    <td align="right">4.94</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">7.04</td>
    <td align="right">7.44</td>
    <td align="right">7.45</td>
    <td align="right">7.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.39</td>
    <td align="right">6.48</td>
    <td align="right">6.51</td>
    <td align="right">6.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.31</td>
    <td align="right">8.12</td>
    <td align="right">8.11</td>
    <td align="right">8.11</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.25</td>
    <td align="right">9.18</td>
    <td align="right">9.27</td>
    <td align="right">9.20</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.43</td>
    <td align="right">12.55</td>
    <td align="right">12.53</td>
    <td align="right">12.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.76</td>
    <td align="right">20.49</td>
    <td align="right">14.69</td>
    <td align="right">24.60</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.08</td>
    <td align="right">26.14</td>
    <td align="right">21.52</td>
    <td align="right">30.81</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.69</td>
    <td align="right">26.16</td>
    <td align="right">21.59</td>
    <td align="right">30.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.95</td>
    <td align="right">23.63</td>
    <td align="right">16.50</td>
    <td align="right">26.87</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.37</td>
    <td align="right">36.46</td>
    <td align="right">24.94</td>
    <td align="right">36.81</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.89</td>
    <td align="right">36.49</td>
    <td align="right">25.07</td>
    <td align="right">36.57</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.34</td>
    <td align="right">4.01</td>
    <td align="right">3.99</td>
    <td align="right">4.03</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.84</td>
    <td align="right">6.99</td>
    <td align="right">7.01</td>
    <td align="right">6.97</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">7.95</td>
    <td align="right">7.92</td>
    <td align="right">7.97</td>
    <td align="right">7.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.93</td>
    <td align="right">8.72</td>
    <td align="right">8.71</td>
    <td align="right">8.69</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.62</td>
    <td align="right">10.65</td>
    <td align="right">10.64</td>
    <td align="right">10.61</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">12.14</td>
    <td align="right">13.14</td>
    <td align="right">13.17</td>
    <td align="right">13.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.61</td>
    <td align="right">20.94</td>
    <td align="right">20.51</td>
    <td align="right">20.64</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.93</td>
    <td align="right">25.66</td>
    <td align="right">25.64</td>
    <td align="right">25.67</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">23.93</td>
    <td align="right">26.06</td>
    <td align="right">26.05</td>
    <td align="right">26.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.88</td>
    <td align="right">23.92</td>
    <td align="right">23.95</td>
    <td align="right">23.92</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.54</td>
    <td align="right">32.00</td>
    <td align="right">32.01</td>
    <td align="right">32.02</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.95</td>
    <td align="right">32.01</td>
    <td align="right">32.03</td>
    <td align="right">32.00</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.12</td>
    <td align="right">9.06</td>
    <td align="right">15.82</td>
    <td align="right">15.04</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.91</td>
    <td align="right">10.70</td>
    <td align="right">21.10</td>
    <td align="right">18.22</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.95</td>
    <td align="right">15.82</td>
    <td align="right">22.95</td>
    <td align="right">20.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.09</td>
    <td align="right">20.10</td>
    <td align="right">19.06</td>
    <td align="right">22.77</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.76</td>
    <td align="right">22.75</td>
    <td align="right">21.43</td>
    <td align="right">26.33</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">28.00</td>
    <td align="right">28.58</td>
    <td align="right">28.91</td>
    <td align="right">28.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.86</td>
    <td align="right">28.33</td>
    <td align="right">21.97</td>
    <td align="right">31.53</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.82</td>
    <td align="right">33.24</td>
    <td align="right">27.52</td>
    <td align="right">36.88</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.01</td>
    <td align="right">45.86</td>
    <td align="right">30.75</td>
    <td align="right">41.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.65</td>
    <td align="right">42.37</td>
    <td align="right">24.90</td>
    <td align="right">42.74</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.12</td>
    <td align="right">50.56</td>
    <td align="right">29.30</td>
    <td align="right">48.75</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.90</td>
    <td align="right">69.40</td>
    <td align="right">38.86</td>
    <td align="right">56.70</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.98</td>
    <td align="right">8.58</td>
    <td align="right">8.56</td>
    <td align="right">8.58</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.68</td>
    <td align="right">10.27</td>
    <td align="right">10.27</td>
    <td align="right">10.38</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.21</td>
    <td align="right">15.47</td>
    <td align="right">15.50</td>
    <td align="right">15.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.47</td>
    <td align="right">18.39</td>
    <td align="right">18.43</td>
    <td align="right">18.43</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">21.30</td>
    <td align="right">20.67</td>
    <td align="right">20.69</td>
    <td align="right">20.67</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">27.48</td>
    <td align="right">28.84</td>
    <td align="right">28.87</td>
    <td align="right">28.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.33</td>
    <td align="right">27.29</td>
    <td align="right">27.27</td>
    <td align="right">27.31</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.90</td>
    <td align="right">39.55</td>
    <td align="right">39.53</td>
    <td align="right">39.51</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.73</td>
    <td align="right">49.98</td>
    <td align="right">49.91</td>
    <td align="right">50.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.66</td>
    <td align="right">42.78</td>
    <td align="right">42.79</td>
    <td align="right">42.76</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.90</td>
    <td align="right">54.52</td>
    <td align="right">52.79</td>
    <td align="right">52.11</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">75.20</td>
    <td align="right">75.17</td>
    <td align="right">75.26</td>
    <td align="right">74.52</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.94</td>
    <td align="right">5.81</td>
    <td align="right">4.24</td>
    <td align="right">12.94</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.37</td>
    <td align="right">10.91</td>
    <td align="right">17.46</td>
    <td align="right">15.40</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.09</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
    <td align="right">4.11</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.06</td>
    <td align="right">4.60</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.64</td>
    <td align="right">16.03</td>
    <td align="right">18.56</td>
    <td align="right">19.74</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.57</td>
    <td align="right">4.68</td>
    <td align="right">4.69</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.00</td>
    <td align="right">19.89</td>
    <td align="right">17.93</td>
    <td align="right">22.26</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.93</td>
    <td align="right">5.72</td>
    <td align="right">5.73</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.68</td>
    <td align="right">24.03</td>
    <td align="right">17.81</td>
    <td align="right">24.76</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.31</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.30</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="right">10.90</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="right">4.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.71</td>
    <td align="right">14.80</td>
    <td align="right">14.80</td>
    <td align="right">14.81</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">4.69</td>
    <td align="right">4.70</td>
    <td align="right">4.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.56</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
    <td align="right">5.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.89</td>
    <td align="right">17.69</td>
    <td align="right">17.75</td>
    <td align="right">17.75</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.00</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="right">5.29</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.92</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.15</td>
    <td align="right">24.82</td>
    <td align="right">24.82</td>
    <td align="right">24.97</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="right">5.74</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.30</td>
    <td align="right">3.44</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.24</td>
    <td align="right">5.86</td>
    <td align="right">13.82</td>
    <td align="right">11.58</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.30</td>
    <td align="right">5.72</td>
    <td align="right">14.28</td>
    <td align="right">11.31</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.89</td>
    <td align="right">2.67</td>
    <td align="right">2.67</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.35</td>
    <td align="right">8.29</td>
    <td align="right">14.46</td>
    <td align="right">13.40</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.05</td>
    <td align="right">8.28</td>
    <td align="right">15.10</td>
    <td align="right">13.37</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.80</td>
    <td align="right">11.69</td>
    <td align="right">15.74</td>
    <td align="right">17.16</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">5.96</td>
    <td align="right">11.44</td>
    <td align="right">15.34</td>
    <td align="right">16.04</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.40</td>
    <td align="right">4.48</td>
    <td align="right">3.35</td>
    <td align="right">13.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.20</td>
    <td align="right">12.96</td>
    <td align="right">15.70</td>
    <td align="right">18.18</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.94</td>
    <td align="right">13.07</td>
    <td align="right">15.53</td>
    <td align="right">17.54</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.43</td>
    <td align="right">4.52</td>
    <td align="right">3.33</td>
    <td align="right">13.92</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.29</td>
    <td align="right">3.87</td>
    <td align="right">3.88</td>
    <td align="right">3.87</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.34</td>
    <td align="right">3.70</td>
    <td align="right">3.72</td>
    <td align="right">3.69</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.89</td>
    <td align="right">2.70</td>
    <td align="right">2.68</td>
    <td align="right">2.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.37</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="right">4.81</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.04</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.81</td>
    <td align="right">7.72</td>
    <td align="right">7.73</td>
    <td align="right">7.71</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.00</td>
    <td align="right">7.52</td>
    <td align="right">7.46</td>
    <td align="right">7.47</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.40</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.17</td>
    <td align="right">8.19</td>
    <td align="right">8.17</td>
    <td align="right">8.17</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.93</td>
    <td align="right">8.33</td>
    <td align="right">8.33</td>
    <td align="right">8.32</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.45</td>
    <td align="right">4.48</td>
    <td align="right">4.49</td>
    <td align="right">4.49</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.85</td>
    <td align="right">2.50</td>
    <td align="right">2.50</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.88</td>
    <td align="right">4.17</td>
    <td align="right">4.20</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.07</td>
    <td align="right">4.01</td>
    <td align="right">4.03</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.97</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="right">3.87</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.26</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.45</td>
    <td align="right">4.21</td>
    <td align="right">3.16</td>
    <td align="right">13.32</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.80</td>
    <td align="right">6.29</td>
    <td align="right">5.17</td>
    <td align="right">16.46</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.01</td>
    <td align="right">6.08</td>
    <td align="right">4.90</td>
    <td align="right">16.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.51</td>
    <td align="right">4.22</td>
    <td align="right">3.14</td>
    <td align="right">13.51</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.89</td>
    <td align="right">7.24</td>
    <td align="right">5.22</td>
    <td align="right">17.05</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.21</td>
    <td align="right">7.00</td>
    <td align="right">5.05</td>
    <td align="right">16.67</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.87</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="right">2.49</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.05</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="right">4.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">3.89</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.25</td>
    <td align="right">4.12</td>
    <td align="right">4.11</td>
    <td align="right">4.11</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="right">4.19</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.80</td>
    <td align="right">6.42</td>
    <td align="right">6.44</td>
    <td align="right">6.42</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.04</td>
    <td align="right">6.21</td>
    <td align="right">6.22</td>
    <td align="right">6.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.50</td>
    <td align="right">4.21</td>
    <td align="right">4.22</td>
    <td align="right">4.21</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.91</td>
    <td align="right">7.33</td>
    <td align="right">7.36</td>
    <td align="right">7.34</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.25</td>
    <td align="right">7.19</td>
    <td align="right">7.19</td>
    <td align="right">7.14</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.32</td>
    <td align="right">6.64</td>
    <td align="right">13.72</td>
    <td align="right">12.50</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">7.85</td>
    <td align="right">18.18</td>
    <td align="right">15.04</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.38</td>
    <td align="right">9.95</td>
    <td align="right">18.75</td>
    <td align="right">15.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.64</td>
    <td align="right">9.07</td>
    <td align="right">13.84</td>
    <td align="right">14.45</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">9.27</td>
    <td align="right">15.38</td>
    <td align="right">16.19</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.97</td>
    <td align="right">13.29</td>
    <td align="right">20.19</td>
    <td align="right">18.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.97</td>
    <td align="right">10.67</td>
    <td align="right">13.52</td>
    <td align="right">15.66</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.52</td>
    <td align="right">11.97</td>
    <td align="right">16.36</td>
    <td align="right">18.46</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.58</td>
    <td align="right">14.52</td>
    <td align="right">18.49</td>
    <td align="right">19.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.37</td>
    <td align="right">13.99</td>
    <td align="right">17.69</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.15</td>
    <td align="right">13.61</td>
    <td align="right">15.75</td>
    <td align="right">19.81</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.86</td>
    <td align="right">20.16</td>
    <td align="right">22.39</td>
    <td align="right">22.83</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.33</td>
    <td align="right">6.65</td>
    <td align="right">6.65</td>
    <td align="right">6.66</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.03</td>
    <td align="right">8.04</td>
    <td align="right">8.03</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.38</td>
    <td align="right">10.49</td>
    <td align="right">10.47</td>
    <td align="right">10.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.60</td>
    <td align="right">9.03</td>
    <td align="right">9.03</td>
    <td align="right">9.03</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.55</td>
    <td align="right">10.29</td>
    <td align="right">10.27</td>
    <td align="right">10.27</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.72</td>
    <td align="right">14.46</td>
    <td align="right">14.46</td>
    <td align="right">14.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.96</td>
    <td align="right">10.85</td>
    <td align="right">10.85</td>
    <td align="right">10.85</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.12</td>
    <td align="right">12.43</td>
    <td align="right">12.43</td>
    <td align="right">12.42</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.77</td>
    <td align="right">15.99</td>
    <td align="right">15.90</td>
    <td align="right">15.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.29</td>
    <td align="right">13.73</td>
    <td align="right">13.72</td>
    <td align="right">13.73</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.16</td>
    <td align="right">15.40</td>
    <td align="right">15.39</td>
    <td align="right">15.40</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.68</td>
    <td align="right">20.91</td>
    <td align="right">21.04</td>
    <td align="right">21.05</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.12</td>
    <td align="right">23.69</td>
    <td align="right">14.34</td>
    <td align="right">31.42</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">16.16</td>
    <td align="right">16.71</td>
    <td align="right">20.60</td>
    <td align="right">19.68</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.55</td>
    <td align="right">5.58</td>
    <td align="right">5.58</td>
    <td align="right">5.62</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.38</td>
    <td align="right">5.96</td>
    <td align="right">5.94</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">50.02</td>
    <td align="right">51.59</td>
    <td align="right">26.82</td>
    <td align="right">40.30</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.22</td>
    <td align="right">11.17</td>
    <td align="right">11.14</td>
    <td align="right">11.19</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.64</td>
    <td align="right">12.68</td>
    <td align="right">12.70</td>
    <td align="right">12.69</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.99</td>
    <td align="right">85.32</td>
    <td align="right">31.72</td>
    <td align="right">60.75</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.06</td>
    <td align="right">18.06</td>
    <td align="right">18.06</td>
    <td align="right">18.07</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.98</td>
    <td align="right">18.76</td>
    <td align="right">18.77</td>
    <td align="right">18.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.29</td>
    <td align="right">119.60</td>
    <td align="right">36.17</td>
    <td align="right">84.50</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.97</td>
    <td align="right">21.71</td>
    <td align="right">21.71</td>
    <td align="right">21.70</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.68</td>
    <td align="right">15.24</td>
    <td align="right">15.24</td>
    <td align="right">15.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">13.50</td>
    <td align="right">14.14</td>
    <td align="right">14.19</td>
    <td align="right">14.18</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.44</td>
    <td align="right">5.47</td>
    <td align="right">5.51</td>
    <td align="right">5.47</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.47</td>
    <td align="right">6.07</td>
    <td align="right">6.09</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.08</td>
    <td align="right">41.81</td>
    <td align="right">41.81</td>
    <td align="right">41.83</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.48</td>
    <td align="right">11.28</td>
    <td align="right">11.29</td>
    <td align="right">11.28</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.78</td>
    <td align="right">11.75</td>
    <td align="right">11.74</td>
    <td align="right">11.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">84.70</td>
    <td align="right">69.77</td>
    <td align="right">69.81</td>
    <td align="right">69.79</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.91</td>
    <td align="right">17.93</td>
    <td align="right">17.95</td>
    <td align="right">17.95</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.94</td>
    <td align="right">18.71</td>
    <td align="right">18.73</td>
    <td align="right">18.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.52</td>
    <td align="right">106.67</td>
    <td align="right">109.20</td>
    <td align="right">107.43</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.95</td>
    <td align="right">21.66</td>
    <td align="right">21.66</td>
    <td align="right">21.65</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.58</td>
    <td align="right">15.09</td>
    <td align="right">15.12</td>
    <td align="right">15.12</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">3.99</td>
    <td align="right">7.07</td>
    <td align="right">14.67</td>
    <td align="right">13.14</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.77</td>
    <td align="right">7.66</td>
    <td align="right">14.92</td>
    <td align="right">13.56</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.88</td>
    <td align="right">3.78</td>
    <td align="right">3.78</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.61</td>
    <td align="right">14.97</td>
    <td align="right">18.72</td>
    <td align="right">19.56</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.79</td>
    <td align="right">17.55</td>
    <td align="right">19.79</td>
    <td align="right">20.74</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.97</td>
    <td align="right">7.64</td>
    <td align="right">7.60</td>
    <td align="right">7.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.24</td>
    <td align="right">29.50</td>
    <td align="right">24.00</td>
    <td align="right">30.56</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.63</td>
    <td align="right">29.50</td>
    <td align="right">23.60</td>
    <td align="right">29.91</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.35</td>
    <td align="right">16.44</td>
    <td align="right">12.57</td>
    <td align="right">21.46</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.07</td>
    <td align="right">38.86</td>
    <td align="right">27.03</td>
    <td align="right">39.01</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.94</td>
    <td align="right">40.33</td>
    <td align="right">27.22</td>
    <td align="right">40.04</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.39</td>
    <td align="right">18.26</td>
    <td align="right">13.93</td>
    <td align="right">23.88</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.73</td>
    <td align="right">5.58</td>
    <td align="right">5.59</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.79</td>
    <td align="right">5.32</td>
    <td align="right">5.31</td>
    <td align="right">5.28</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.54</td>
    <td align="right">3.45</td>
    <td align="right">3.43</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.18</td>
    <td align="right">10.00</td>
    <td align="right">10.47</td>
    <td align="right">10.19</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.81</td>
    <td align="right">12.35</td>
    <td align="right">12.30</td>
    <td align="right">12.32</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.85</td>
    <td align="right">7.52</td>
    <td align="right">7.53</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.25</td>
    <td align="right">22.23</td>
    <td align="right">22.25</td>
    <td align="right">22.25</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.57</td>
    <td align="right">22.34</td>
    <td align="right">22.29</td>
    <td align="right">22.31</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.21</td>
    <td align="right">16.28</td>
    <td align="right">16.29</td>
    <td align="right">16.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.01</td>
    <td align="right">29.62</td>
    <td align="right">29.63</td>
    <td align="right">29.65</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.90</td>
    <td align="right">30.71</td>
    <td align="right">32.68</td>
    <td align="right">32.37</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.39</td>
    <td align="right">18.20</td>
    <td align="right">18.20</td>
    <td align="right">18.20</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.34</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="right">2.91</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.83</td>
    <td align="right">5.16</td>
    <td align="right">5.16</td>
    <td align="right">5.10</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.08</td>
    <td align="right">5.26</td>
    <td align="right">5.32</td>
    <td align="right">5.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.30</td>
    <td align="right">7.28</td>
    <td align="right">7.30</td>
    <td align="right">7.29</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.63</td>
    <td align="right">10.10</td>
    <td align="right">10.08</td>
    <td align="right">10.10</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.59</td>
    <td align="right">11.86</td>
    <td align="right">11.87</td>
    <td align="right">11.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.32</td>
    <td align="right">15.99</td>
    <td align="right">11.84</td>
    <td align="right">20.48</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.29</td>
    <td align="right">21.57</td>
    <td align="right">17.24</td>
    <td align="right">27.72</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.43</td>
    <td align="right">21.66</td>
    <td align="right">17.32</td>
    <td align="right">27.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.69</td>
    <td align="right">18.22</td>
    <td align="right">13.47</td>
    <td align="right">23.28</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.14</td>
    <td align="right">29.39</td>
    <td align="right">20.08</td>
    <td align="right">32.53</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.62</td>
    <td align="right">27.05</td>
    <td align="right">20.14</td>
    <td align="right">31.85</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.59</td>
    <td align="right">3.33</td>
    <td align="right">3.37</td>
    <td align="right">3.34</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.82</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="right">5.32</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.36</td>
    <td align="right">5.60</td>
    <td align="right">5.59</td>
    <td align="right">5.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.46</td>
    <td align="right">7.44</td>
    <td align="right">7.43</td>
    <td align="right">7.43</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.76</td>
    <td align="right">10.42</td>
    <td align="right">10.43</td>
    <td align="right">10.43</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">9.59</td>
    <td align="right">10.72</td>
    <td align="right">10.74</td>
    <td align="right">10.70</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.46</td>
    <td align="right">16.05</td>
    <td align="right">16.04</td>
    <td align="right">16.04</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.98</td>
    <td align="right">21.55</td>
    <td align="right">21.64</td>
    <td align="right">21.55</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.67</td>
    <td align="right">21.19</td>
    <td align="right">21.19</td>
    <td align="right">21.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.67</td>
    <td align="right">18.15</td>
    <td align="right">18.16</td>
    <td align="right">18.16</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.02</td>
    <td align="right">29.94</td>
    <td align="right">30.02</td>
    <td align="right">29.97</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.44</td>
    <td align="right">29.16</td>
    <td align="right">29.15</td>
    <td align="right">29.15</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.19</td>
    <td align="right">8.47</td>
    <td align="right">15.37</td>
    <td align="right">14.84</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.66</td>
    <td align="right">9.40</td>
    <td align="right">19.58</td>
    <td align="right">17.00</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">15.28</td>
    <td align="right">14.63</td>
    <td align="right">21.16</td>
    <td align="right">18.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">20.02</td>
    <td align="right">18.33</td>
    <td align="right">19.08</td>
    <td align="right">22.73</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.66</td>
    <td align="right">18.67</td>
    <td align="right">19.14</td>
    <td align="right">23.45</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">27.49</td>
    <td align="right">25.60</td>
    <td align="right">25.55</td>
    <td align="right">26.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.71</td>
    <td align="right">26.43</td>
    <td align="right">21.66</td>
    <td align="right">28.94</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">35.72</td>
    <td align="right">32.23</td>
    <td align="right">24.57</td>
    <td align="right">34.66</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.39</td>
    <td align="right">42.26</td>
    <td align="right">29.31</td>
    <td align="right">38.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.10</td>
    <td align="right">35.67</td>
    <td align="right">24.15</td>
    <td align="right">39.00</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.28</td>
    <td align="right">39.99</td>
    <td align="right">26.41</td>
    <td align="right">43.38</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.58</td>
    <td align="right">65.83</td>
    <td align="right">39.74</td>
    <td align="right">55.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.13</td>
    <td align="right">8.58</td>
    <td align="right">8.56</td>
    <td align="right">8.57</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.07</td>
    <td align="right">10.53</td>
    <td align="right">10.57</td>
    <td align="right">10.55</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.12</td>
    <td align="right">14.08</td>
    <td align="right">14.07</td>
    <td align="right">14.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.76</td>
    <td align="right">16.86</td>
    <td align="right">16.89</td>
    <td align="right">16.82</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.06</td>
    <td align="right">20.13</td>
    <td align="right">20.12</td>
    <td align="right">20.04</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">31.71</td>
    <td align="right">33.01</td>
    <td align="right">33.01</td>
    <td align="right">33.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.80</td>
    <td align="right">30.62</td>
    <td align="right">30.66</td>
    <td align="right">30.58</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.37</td>
    <td align="right">38.48</td>
    <td align="right">38.49</td>
    <td align="right">38.46</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.82</td>
    <td align="right">48.50</td>
    <td align="right">48.36</td>
    <td align="right">48.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">42.79</td>
    <td align="right">41.98</td>
    <td align="right">41.96</td>
    <td align="right">41.99</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.49</td>
    <td align="right">50.89</td>
    <td align="right">50.96</td>
    <td align="right">50.87</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.34</td>
    <td align="right">72.68</td>
    <td align="right">76.12</td>
    <td align="right">76.98</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.59</td>
    <td align="right">2.58</td>
    <td align="right">1.96</td>
    <td align="right">9.52</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.37</td>
    <td align="right">4.21</td>
    <td align="right">11.40</td>
    <td align="right">8.83</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.31</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">1.29</td>
    <td align="right">1.28</td>
    <td align="right">1.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.49</td>
    <td align="right">6.06</td>
    <td align="right">11.96</td>
    <td align="right">10.46</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.40</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.68</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.58</td>
    <td align="right">7.31</td>
    <td align="right">11.14</td>
    <td align="right">11.01</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.60</td>
    <td align="right">1.63</td>
    <td align="right">1.63</td>
    <td align="right">1.65</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.74</td>
    <td align="right">1.60</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.90</td>
    <td align="right">9.40</td>
    <td align="right">11.42</td>
    <td align="right">12.51</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.80</td>
    <td align="right">1.80</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.35</td>
    <td align="right">3.85</td>
    <td align="right">3.86</td>
    <td align="right">3.86</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.30</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="right">1.23</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.45</td>
    <td align="right">5.77</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.70</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.56</td>
    <td align="right">7.06</td>
    <td align="right">7.06</td>
    <td align="right">7.06</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.93</td>
    <td align="right">9.08</td>
    <td align="right">9.08</td>
    <td align="right">9.08</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.81</td>
    <td align="right">1.82</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.30</td>
    <td align="right">2.59</td>
    <td align="right">9.44</td>
    <td align="right">7.41</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.28</td>
    <td align="right">2.59</td>
    <td align="right">8.83</td>
    <td align="right">7.06</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.03</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">3.93</td>
    <td align="right">10.87</td>
    <td align="right">8.94</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">3.58</td>
    <td align="right">9.75</td>
    <td align="right">8.24</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.41</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.11</td>
    <td align="right">4.95</td>
    <td align="right">10.65</td>
    <td align="right">9.51</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">4.86</td>
    <td align="right">10.11</td>
    <td align="right">8.96</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.91</td>
    <td align="right">2.41</td>
    <td align="right">1.75</td>
    <td align="right">11.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.58</td>
    <td align="right">5.60</td>
    <td align="right">10.31</td>
    <td align="right">9.78</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.77</td>
    <td align="right">5.88</td>
    <td align="right">10.25</td>
    <td align="right">9.61</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="right">1.72</td>
    <td align="right">11.42</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.29</td>
    <td align="right">1.75</td>
    <td align="right">1.73</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">1.68</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.74</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.40</td>
    <td align="right">1.41</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.12</td>
    <td align="right">2.92</td>
    <td align="right">2.91</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.12</td>
    <td align="right">3.04</td>
    <td align="right">3.03</td>
    <td align="right">3.04</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.93</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.62</td>
    <td align="right">3.35</td>
    <td align="right">3.41</td>
    <td align="right">3.41</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.79</td>
    <td align="right">3.61</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">3.01</td>
    <td align="right">2.93</td>
    <td align="right">2.92</td>
    <td align="right">2.92</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.04</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.25</td>
    <td align="right">2.59</td>
    <td align="right">9.39</td>
    <td align="right">7.42</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.33</td>
    <td align="right">2.60</td>
    <td align="right">8.89</td>
    <td align="right">7.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.06</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
    <td align="right">1.62</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.21</td>
    <td align="right">3.98</td>
    <td align="right">10.97</td>
    <td align="right">8.98</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">3.58</td>
    <td align="right">9.74</td>
    <td align="right">8.25</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.85</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
    <td align="right">11.28</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">4.97</td>
    <td align="right">10.71</td>
    <td align="right">9.54</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">4.84</td>
    <td align="right">10.06</td>
    <td align="right">8.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.90</td>
    <td align="right">2.88</td>
    <td align="right">1.73</td>
    <td align="right">11.37</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.52</td>
    <td align="right">5.63</td>
    <td align="right">10.30</td>
    <td align="right">9.78</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.65</td>
    <td align="right">5.90</td>
    <td align="right">10.30</td>
    <td align="right">9.67</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.02</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="right">1.67</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.29</td>
    <td align="right">1.72</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.31</td>
    <td align="right">1.75</td>
    <td align="right">1.75</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.04</td>
    <td align="right">1.58</td>
    <td align="right">1.59</td>
    <td align="right">1.58</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.72</td>
    <td align="right">2.17</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.87</td>
    <td align="right">2.34</td>
    <td align="right">2.35</td>
    <td align="right">2.35</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.06</td>
    <td align="right">2.92</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
    <td align="right">3.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.87</td>
    <td align="right">2.84</td>
    <td align="right">2.83</td>
    <td align="right">2.82</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.63</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
    <td align="right">3.34</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.76</td>
    <td align="right">3.56</td>
    <td align="right">3.55</td>
    <td align="right">3.55</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.21</td>
    <td align="right">3.26</td>
    <td align="right">10.17</td>
    <td align="right">8.49</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.95</td>
    <td align="right">3.87</td>
    <td align="right">12.72</td>
    <td align="right">9.32</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.70</td>
    <td align="right">5.18</td>
    <td align="right">13.16</td>
    <td align="right">9.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.39</td>
    <td align="right">4.36</td>
    <td align="right">10.00</td>
    <td align="right">9.49</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.42</td>
    <td align="right">4.52</td>
    <td align="right">10.44</td>
    <td align="right">10.08</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.92</td>
    <td align="right">7.17</td>
    <td align="right">13.59</td>
    <td align="right">11.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.52</td>
    <td align="right">5.25</td>
    <td align="right">9.76</td>
    <td align="right">9.95</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.54</td>
    <td align="right">5.77</td>
    <td align="right">11.32</td>
    <td align="right">10.95</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.05</td>
    <td align="right">7.91</td>
    <td align="right">12.48</td>
    <td align="right">11.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.02</td>
    <td align="right">6.33</td>
    <td align="right">10.25</td>
    <td align="right">10.49</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.39</td>
    <td align="right">6.40</td>
    <td align="right">10.77</td>
    <td align="right">11.23</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.20</td>
    <td align="right">10.73</td>
    <td align="right">14.51</td>
    <td align="right">14.12</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.22</td>
    <td align="right">2.86</td>
    <td align="right">2.87</td>
    <td align="right">2.86</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.94</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="right">3.82</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.68</td>
    <td align="right">4.87</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.38</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="right">3.83</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.37</td>
    <td align="right">4.30</td>
    <td align="right">4.29</td>
    <td align="right">4.25</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.90</td>
    <td align="right">6.79</td>
    <td align="right">6.80</td>
    <td align="right">6.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.49</td>
    <td align="right">4.57</td>
    <td align="right">4.56</td>
    <td align="right">4.56</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.50</td>
    <td align="right">5.27</td>
    <td align="right">5.30</td>
    <td align="right">5.25</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.03</td>
    <td align="right">7.54</td>
    <td align="right">7.54</td>
    <td align="right">7.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.00</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="right">5.79</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.37</td>
    <td align="right">6.03</td>
    <td align="right">6.04</td>
    <td align="right">6.09</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.11</td>
    <td align="right">10.59</td>
    <td align="right">10.60</td>
    <td align="right">10.60</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.80</td>
    <td align="right">11.21</td>
    <td align="right">6.11</td>
    <td align="right">15.51</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.73</td>
    <td align="right">6.25</td>
    <td align="right">13.05</td>
    <td align="right">10.48</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.11</td>
    <td align="right">1.99</td>
    <td align="right">2.02</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.13</td>
    <td align="right">2.08</td>
    <td align="right">2.08</td>
    <td align="right">2.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.88</td>
    <td align="right">11.07</td>
    <td align="right">16.28</td>
    <td align="right">14.97</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.23</td>
    <td align="right">3.50</td>
    <td align="right">3.51</td>
    <td align="right">3.91</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.25</td>
    <td align="right">3.17</td>
    <td align="right">3.16</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.15</td>
    <td align="right">24.47</td>
    <td align="right">18.50</td>
    <td align="right">22.40</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.77</td>
    <td align="right">6.30</td>
    <td align="right">6.32</td>
    <td align="right">6.20</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.31</td>
    <td align="right">5.75</td>
    <td align="right">5.79</td>
    <td align="right">5.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.22</td>
    <td align="right">39.48</td>
    <td align="right">20.44</td>
    <td align="right">31.39</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.16</td>
    <td align="right">8.21</td>
    <td align="right">8.01</td>
    <td align="right">8.38</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.60</td>
    <td align="right">6.50</td>
    <td align="right">6.90</td>
    <td align="right">6.67</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.76</td>
    <td align="right">6.59</td>
    <td align="right">6.60</td>
    <td align="right">6.56</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.09</td>
    <td align="right">2.02</td>
    <td align="right">2.00</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.14</td>
    <td align="right">2.08</td>
    <td align="right">2.09</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.30</td>
    <td align="right">12.66</td>
    <td align="right">12.36</td>
    <td align="right">12.72</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.65</td>
    <td align="right">3.56</td>
    <td align="right">3.50</td>
    <td align="right">3.43</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.51</td>
    <td align="right">3.47</td>
    <td align="right">3.56</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">29.57</td>
    <td align="right">24.84</td>
    <td align="right">26.69</td>
    <td align="right">28.37</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.97</td>
    <td align="right">6.75</td>
    <td align="right">6.58</td>
    <td align="right">6.24</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.44</td>
    <td align="right">6.41</td>
    <td align="right">6.31</td>
    <td align="right">6.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.81</td>
    <td align="right">43.73</td>
    <td align="right">45.49</td>
    <td align="right">45.66</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.25</td>
    <td align="right">7.96</td>
    <td align="right">8.20</td>
    <td align="right">8.21</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.27</td>
    <td align="right">6.39</td>
    <td align="right">6.84</td>
    <td align="right">6.56</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.74</td>
    <td align="right">3.48</td>
    <td align="right">10.31</td>
    <td align="right">8.45</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.82</td>
    <td align="right">3.56</td>
    <td align="right">9.82</td>
    <td align="right">8.21</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.43</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.13</td>
    <td align="right">7.51</td>
    <td align="right">14.10</td>
    <td align="right">13.06</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.47</td>
    <td align="right">6.81</td>
    <td align="right">12.33</td>
    <td align="right">11.59</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">3.21</td>
    <td align="right">3.56</td>
    <td align="right">3.43</td>
    <td align="right">3.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.99</td>
    <td align="right">14.18</td>
    <td align="right">15.88</td>
    <td align="right">17.00</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.90</td>
    <td align="right">13.92</td>
    <td align="right">15.28</td>
    <td align="right">16.18</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.34</td>
    <td align="right">8.82</td>
    <td align="right">5.90</td>
    <td align="right">15.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.02</td>
    <td align="right">19.05</td>
    <td align="right">15.76</td>
    <td align="right">19.50</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.63</td>
    <td align="right">17.58</td>
    <td align="right">15.83</td>
    <td align="right">20.16</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.25</td>
    <td align="right">10.13</td>
    <td align="right">6.23</td>
    <td align="right">16.22</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.69</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.71</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.38</td>
    <td align="right">2.53</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.66</td>
    <td align="right">3.94</td>
    <td align="right">3.92</td>
    <td align="right">3.91</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.11</td>
    <td align="right">4.59</td>
    <td align="right">4.46</td>
    <td align="right">4.44</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.62</td>
    <td align="right">3.21</td>
    <td align="right">3.20</td>
    <td align="right">3.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.67</td>
    <td align="right">8.94</td>
    <td align="right">8.94</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.74</td>
    <td align="right">8.83</td>
    <td align="right">8.84</td>
    <td align="right">8.84</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.37</td>
    <td align="right">7.48</td>
    <td align="right">7.57</td>
    <td align="right">7.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.15</td>
    <td align="right">11.85</td>
    <td align="right">12.14</td>
    <td align="right">12.15</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.63</td>
    <td align="right">12.59</td>
    <td align="right">12.79</td>
    <td align="right">12.78</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.19</td>
    <td align="right">10.19</td>
    <td align="right">10.66</td>
    <td align="right">10.65</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.36</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="right">2.52</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.69</td>
    <td align="right">3.43</td>
    <td align="right">10.22</td>
    <td align="right">8.44</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.71</td>
    <td align="right">3.47</td>
    <td align="right">9.70</td>
    <td align="right">8.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.85</td>
    <td align="right">3.09</td>
    <td align="right">3.07</td>
    <td align="right">3.05</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.66</td>
    <td align="right">6.53</td>
    <td align="right">13.30</td>
    <td align="right">12.19</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.13</td>
    <td align="right">6.54</td>
    <td align="right">11.87</td>
    <td align="right">11.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.32</td>
    <td align="right">7.46</td>
    <td align="right">5.20</td>
    <td align="right">14.19</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.62</td>
    <td align="right">12.53</td>
    <td align="right">14.75</td>
    <td align="right">15.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.66</td>
    <td align="right">12.51</td>
    <td align="right">14.23</td>
    <td align="right">15.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.32</td>
    <td align="right">10.09</td>
    <td align="right">6.31</td>
    <td align="right">15.99</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.14</td>
    <td align="right">16.78</td>
    <td align="right">15.34</td>
    <td align="right">19.42</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.64</td>
    <td align="right">17.60</td>
    <td align="right">15.82</td>
    <td align="right">20.15</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.36</td>
    <td align="right">2.51</td>
    <td align="right">2.52</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.69</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.71</td>
    <td align="right">2.59</td>
    <td align="right">2.60</td>
    <td align="right">2.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.86</td>
    <td align="right">3.09</td>
    <td align="right">3.06</td>
    <td align="right">3.06</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.64</td>
    <td align="right">3.96</td>
    <td align="right">3.93</td>
    <td align="right">3.92</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.12</td>
    <td align="right">4.64</td>
    <td align="right">4.46</td>
    <td align="right">4.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.41</td>
    <td align="right">7.55</td>
    <td align="right">7.56</td>
    <td align="right">7.54</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.64</td>
    <td align="right">8.95</td>
    <td align="right">8.96</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.60</td>
    <td align="right">8.83</td>
    <td align="right">8.85</td>
    <td align="right">8.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.45</td>
    <td align="right">10.32</td>
    <td align="right">10.69</td>
    <td align="right">10.68</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.15</td>
    <td align="right">11.80</td>
    <td align="right">12.19</td>
    <td align="right">12.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.62</td>
    <td align="right">12.56</td>
    <td align="right">12.78</td>
    <td align="right">12.79</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.59</td>
    <td align="right">4.29</td>
    <td align="right">11.25</td>
    <td align="right">9.82</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.78</td>
    <td align="right">4.91</td>
    <td align="right">13.57</td>
    <td align="right">10.53</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.97</td>
    <td align="right">6.80</td>
    <td align="right">14.68</td>
    <td align="right">11.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.00</td>
    <td align="right">7.26</td>
    <td align="right">12.09</td>
    <td align="right">12.80</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.28</td>
    <td align="right">7.67</td>
    <td align="right">12.49</td>
    <td align="right">13.46</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.16</td>
    <td align="right">11.53</td>
    <td align="right">17.47</td>
    <td align="right">15.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.12</td>
    <td align="right">12.13</td>
    <td align="right">13.48</td>
    <td align="right">16.23</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.44</td>
    <td align="right">14.12</td>
    <td align="right">15.83</td>
    <td align="right">18.55</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.31</td>
    <td align="right">18.95</td>
    <td align="right">18.24</td>
    <td align="right">19.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.51</td>
    <td align="right">16.24</td>
    <td align="right">15.08</td>
    <td align="right">20.07</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.22</td>
    <td align="right">18.94</td>
    <td align="right">16.58</td>
    <td align="right">23.01</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.62</td>
    <td align="right">34.35</td>
    <td align="right">26.68</td>
    <td align="right">31.69</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.59</td>
    <td align="right">4.21</td>
    <td align="right">4.23</td>
    <td align="right">4.26</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.78</td>
    <td align="right">5.19</td>
    <td align="right">5.19</td>
    <td align="right">5.20</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">8.97</td>
    <td align="right">6.86</td>
    <td align="right">6.89</td>
    <td align="right">6.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.03</td>
    <td align="right">7.61</td>
    <td align="right">7.62</td>
    <td align="right">7.63</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.29</td>
    <td align="right">7.97</td>
    <td align="right">7.94</td>
    <td align="right">7.92</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.17</td>
    <td align="right">11.88</td>
    <td align="right">11.78</td>
    <td align="right">11.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.16</td>
    <td align="right">13.00</td>
    <td align="right">13.14</td>
    <td align="right">13.20</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.68</td>
    <td align="right">15.04</td>
    <td align="right">15.13</td>
    <td align="right">15.24</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.47</td>
    <td align="right">20.19</td>
    <td align="right">20.27</td>
    <td align="right">20.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.57</td>
    <td align="right">17.77</td>
    <td align="right">18.27</td>
    <td align="right">18.21</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.13</td>
    <td align="right">20.59</td>
    <td align="right">21.07</td>
    <td align="right">21.09</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.60</td>
    <td align="right">35.55</td>
    <td align="right">35.62</td>
    <td align="right">35.55</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.16</td>
    <td align="right">5.23</td>
    <td align="right">3.52</td>
    <td align="right">9.95</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.28</td>
    <td align="right">11.32</td>
    <td align="right">14.27</td>
    <td align="right">13.85</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.63</td>
    <td align="right">3.62</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">4.18</td>
    <td align="right">4.17</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.14</td>
    <td align="right">16.07</td>
    <td align="right">15.08</td>
    <td align="right">16.98</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.44</td>
    <td align="right">4.09</td>
    <td align="right">4.08</td>
    <td align="right">4.05</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">4.72</td>
    <td align="right">4.70</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.26</td>
    <td align="right">20.51</td>
    <td align="right">14.27</td>
    <td align="right">19.82</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.08</td>
    <td align="right">4.43</td>
    <td align="right">4.42</td>
    <td align="right">4.36</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">5.11</td>
    <td align="right">5.10</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.93</td>
    <td align="right">25.07</td>
    <td align="right">14.56</td>
    <td align="right">22.15</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.74</td>
    <td align="right">4.79</td>
    <td align="right">4.79</td>
    <td align="right">4.78</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.28</td>
    <td align="right">5.58</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.31</td>
    <td align="right">12.56</td>
    <td align="right">12.60</td>
    <td align="right">12.57</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.65</td>
    <td align="right">3.64</td>
    <td align="right">3.65</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.39</td>
    <td align="right">4.17</td>
    <td align="right">4.15</td>
    <td align="right">4.15</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.14</td>
    <td align="right">18.48</td>
    <td align="right">18.40</td>
    <td align="right">18.35</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.41</td>
    <td align="right">4.08</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.77</td>
    <td align="right">4.74</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.27</td>
    <td align="right">22.45</td>
    <td align="right">22.38</td>
    <td align="right">22.38</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.07</td>
    <td align="right">4.43</td>
    <td align="right">4.41</td>
    <td align="right">4.39</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.68</td>
    <td align="right">5.14</td>
    <td align="right">5.14</td>
    <td align="right">5.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.06</td>
    <td align="right">28.00</td>
    <td align="right">27.74</td>
    <td align="right">27.59</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.74</td>
    <td align="right">4.81</td>
    <td align="right">4.80</td>
    <td align="right">4.79</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.27</td>
    <td align="right">5.56</td>
    <td align="right">5.53</td>
    <td align="right">5.52</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.41</td>
    <td align="right">6.79</td>
    <td align="right">11.11</td>
    <td align="right">10.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.48</td>
    <td align="right">7.31</td>
    <td align="right">12.14</td>
    <td align="right">11.63</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
    <td align="right">2.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.26</td>
    <td align="right">9.62</td>
    <td align="right">11.73</td>
    <td align="right">12.40</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.72</td>
    <td align="right">11.22</td>
    <td align="right">13.07</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.83</td>
    <td align="right">2.98</td>
    <td align="right">2.38</td>
    <td align="right">9.05</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.60</td>
    <td align="right">12.85</td>
    <td align="right">14.20</td>
    <td align="right">15.51</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.24</td>
    <td align="right">13.88</td>
    <td align="right">15.46</td>
    <td align="right">16.46</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.31</td>
    <td align="right">4.47</td>
    <td align="right">3.14</td>
    <td align="right">11.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.64</td>
    <td align="right">14.33</td>
    <td align="right">13.34</td>
    <td align="right">16.68</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.09</td>
    <td align="right">18.44</td>
    <td align="right">15.53</td>
    <td align="right">20.34</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.31</td>
    <td align="right">4.47</td>
    <td align="right">3.08</td>
    <td align="right">11.22</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.42</td>
    <td align="right">4.31</td>
    <td align="right">4.34</td>
    <td align="right">4.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">7.48</td>
    <td align="right">4.66</td>
    <td align="right">4.66</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.87</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.29</td>
    <td align="right">7.03</td>
    <td align="right">7.01</td>
    <td align="right">6.95</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.77</td>
    <td align="right">7.09</td>
    <td align="right">7.09</td>
    <td align="right">7.07</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">2.18</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.62</td>
    <td align="right">9.31</td>
    <td align="right">9.29</td>
    <td align="right">9.10</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.22</td>
    <td align="right">10.51</td>
    <td align="right">10.41</td>
    <td align="right">10.47</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.30</td>
    <td align="right">3.50</td>
    <td align="right">3.47</td>
    <td align="right">3.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.70</td>
    <td align="right">10.39</td>
    <td align="right">10.36</td>
    <td align="right">10.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">14.09</td>
    <td align="right">12.25</td>
    <td align="right">12.20</td>
    <td align="right">12.18</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.32</td>
    <td align="right">3.50</td>
    <td align="right">3.49</td>
    <td align="right">3.49</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.79</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.72</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.77</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.25</td>
    <td align="right">3.36</td>
    <td align="right">2.72</td>
    <td align="right">9.60</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.89</td>
    <td align="right">3.26</td>
    <td align="right">10.39</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">4.59</td>
    <td align="right">3.92</td>
    <td align="right">11.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.45</td>
    <td align="right">4.37</td>
    <td align="right">2.99</td>
    <td align="right">10.59</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.94</td>
    <td align="right">6.42</td>
    <td align="right">5.06</td>
    <td align="right">13.36</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.72</td>
    <td align="right">6.31</td>
    <td align="right">5.02</td>
    <td align="right">12.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.43</td>
    <td align="right">4.37</td>
    <td align="right">3.03</td>
    <td align="right">10.65</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.86</td>
    <td align="right">7.06</td>
    <td align="right">5.07</td>
    <td align="right">13.75</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.06</td>
    <td align="right">6.89</td>
    <td align="right">5.09</td>
    <td align="right">13.33</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.81</td>
    <td align="right">2.05</td>
    <td align="right">2.04</td>
    <td align="right">2.05</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.72</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
    <td align="right">3.27</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.78</td>
    <td align="right">3.13</td>
    <td align="right">3.13</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.24</td>
    <td align="right">2.07</td>
    <td align="right">2.06</td>
    <td align="right">2.05</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">4.42</td>
    <td align="right">4.39</td>
    <td align="right">4.37</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.69</td>
    <td align="right">5.14</td>
    <td align="right">5.10</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">3.30</td>
    <td align="right">3.29</td>
    <td align="right">3.28</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.93</td>
    <td align="right">6.62</td>
    <td align="right">6.60</td>
    <td align="right">6.58</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.71</td>
    <td align="right">6.45</td>
    <td align="right">6.43</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">3.31</td>
    <td align="right">3.30</td>
    <td align="right">3.29</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.87</td>
    <td align="right">7.64</td>
    <td align="right">7.62</td>
    <td align="right">7.60</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.06</td>
    <td align="right">7.30</td>
    <td align="right">7.26</td>
    <td align="right">7.25</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.09</td>
    <td align="right">6.76</td>
    <td align="right">11.02</td>
    <td align="right">10.56</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.17</td>
    <td align="right">8.96</td>
    <td align="right">14.20</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.11</td>
    <td align="right">12.25</td>
    <td align="right">16.36</td>
    <td align="right">14.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.47</td>
    <td align="right">10.01</td>
    <td align="right">12.05</td>
    <td align="right">13.36</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.87</td>
    <td align="right">11.24</td>
    <td align="right">13.17</td>
    <td align="right">14.65</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.70</td>
    <td align="right">16.03</td>
    <td align="right">16.37</td>
    <td align="right">16.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.39</td>
    <td align="right">11.56</td>
    <td align="right">11.88</td>
    <td align="right">14.23</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.29</td>
    <td align="right">13.39</td>
    <td align="right">12.71</td>
    <td align="right">15.68</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.57</td>
    <td align="right">17.37</td>
    <td align="right">16.96</td>
    <td align="right">18.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.68</td>
    <td align="right">14.00</td>
    <td align="right">12.34</td>
    <td align="right">16.55</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.37</td>
    <td align="right">15.14</td>
    <td align="right">12.43</td>
    <td align="right">16.96</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.49</td>
    <td align="right">23.71</td>
    <td align="right">19.17</td>
    <td align="right">22.25</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.09</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.86</td>
    <td align="right">7.40</td>
    <td align="right">7.40</td>
    <td align="right">7.41</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.09</td>
    <td align="right">8.91</td>
    <td align="right">9.00</td>
    <td align="right">9.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.44</td>
    <td align="right">8.09</td>
    <td align="right">8.05</td>
    <td align="right">8.00</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.95</td>
    <td align="right">9.20</td>
    <td align="right">9.13</td>
    <td align="right">9.00</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.75</td>
    <td align="right">12.70</td>
    <td align="right">12.67</td>
    <td align="right">12.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.45</td>
    <td align="right">10.73</td>
    <td align="right">10.69</td>
    <td align="right">10.66</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.34</td>
    <td align="right">12.76</td>
    <td align="right">12.70</td>
    <td align="right">12.69</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.64</td>
    <td align="right">14.85</td>
    <td align="right">14.81</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.72</td>
    <td align="right">12.71</td>
    <td align="right">12.66</td>
    <td align="right">12.55</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.42</td>
    <td align="right">14.18</td>
    <td align="right">14.17</td>
    <td align="right">14.14</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.56</td>
    <td align="right">23.09</td>
    <td align="right">23.03</td>
    <td align="right">22.73</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.99</td>
    <td align="right">23.36</td>
    <td align="right">12.01</td>
    <td align="right">27.78</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.97</td>
    <td align="right">11.86</td>
    <td align="right">15.67</td>
    <td align="right">15.08</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">11.15</td>
    <td align="right">10.94</td>
    <td align="right">10.95</td>
    <td align="right">10.94</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.74</td>
    <td align="right">4.58</td>
    <td align="right">4.52</td>
    <td align="right">4.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">25.16</td>
    <td align="right">26.12</td>
    <td align="right">17.89</td>
    <td align="right">23.45</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">8.08</td>
    <td align="right">7.66</td>
    <td align="right">7.41</td>
    <td align="right">7.59</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">9.33</td>
    <td align="right">9.17</td>
    <td align="right">9.07</td>
    <td align="right">9.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">69.77</td>
    <td align="right">82.69</td>
    <td align="right">26.85</td>
    <td align="right">57.06</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.61</td>
    <td align="right">14.00</td>
    <td align="right">13.97</td>
    <td align="right">13.90</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.39</td>
    <td align="right">15.92</td>
    <td align="right">16.03</td>
    <td align="right">16.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.92</td>
    <td align="right">121.94</td>
    <td align="right">31.66</td>
    <td align="right">79.81</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.63</td>
    <td align="right">18.59</td>
    <td align="right">18.75</td>
    <td align="right">18.72</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.86</td>
    <td align="right">22.53</td>
    <td align="right">22.57</td>
    <td align="right">22.64</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.94</td>
    <td align="right">13.06</td>
    <td align="right">13.09</td>
    <td align="right">13.01</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.22</td>
    <td align="right">3.91</td>
    <td align="right">3.85</td>
    <td align="right">3.86</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.76</td>
    <td align="right">4.61</td>
    <td align="right">4.51</td>
    <td align="right">4.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">31.65</td>
    <td align="right">37.80</td>
    <td align="right">37.84</td>
    <td align="right">37.90</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">13.60</td>
    <td align="right">13.22</td>
    <td align="right">13.23</td>
    <td align="right">13.20</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">8.04</td>
    <td align="right">7.83</td>
    <td align="right">7.37</td>
    <td align="right">7.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">68.65</td>
    <td align="right">86.80</td>
    <td align="right">86.80</td>
    <td align="right">86.83</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.32</td>
    <td align="right">13.71</td>
    <td align="right">13.89</td>
    <td align="right">13.82</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.44</td>
    <td align="right">15.94</td>
    <td align="right">15.98</td>
    <td align="right">15.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.55</td>
    <td align="right">128.11</td>
    <td align="right">127.88</td>
    <td align="right">128.11</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.54</td>
    <td align="right">18.70</td>
    <td align="right">18.73</td>
    <td align="right">18.63</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.76</td>
    <td align="right">22.66</td>
    <td align="right">22.71</td>
    <td align="right">22.78</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.12</td>
    <td align="right">7.50</td>
    <td align="right">11.77</td>
    <td align="right">11.58</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.71</td>
    <td align="right">7.94</td>
    <td align="right">12.99</td>
    <td align="right">12.26</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.29</td>
    <td align="right">2.47</td>
    <td align="right">2.33</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">12.06</td>
    <td align="right">13.95</td>
    <td align="right">14.42</td>
    <td align="right">16.14</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.80</td>
    <td align="right">18.07</td>
    <td align="right">15.60</td>
    <td align="right">19.97</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">6.55</td>
    <td align="right">6.76</td>
    <td align="right">5.89</td>
    <td align="right">11.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.19</td>
    <td align="right">30.04</td>
    <td align="right">22.06</td>
    <td align="right">29.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.90</td>
    <td align="right">31.42</td>
    <td align="right">25.63</td>
    <td align="right">32.90</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.25</td>
    <td align="right">15.57</td>
    <td align="right">11.03</td>
    <td align="right">17.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.02</td>
    <td align="right">39.68</td>
    <td align="right">24.19</td>
    <td align="right">38.22</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.03</td>
    <td align="right">56.32</td>
    <td align="right">30.19</td>
    <td align="right">53.32</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.30</td>
    <td align="right">17.86</td>
    <td align="right">12.39</td>
    <td align="right">20.17</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.10</td>
    <td align="right">4.68</td>
    <td align="right">4.62</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.67</td>
    <td align="right">5.02</td>
    <td align="right">5.06</td>
    <td align="right">5.04</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.72</td>
    <td align="right">3.73</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">11.91</td>
    <td align="right">10.89</td>
    <td align="right">10.57</td>
    <td align="right">10.63</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">17.61</td>
    <td align="right">12.01</td>
    <td align="right">11.73</td>
    <td align="right">11.90</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.67</td>
    <td align="right">5.05</td>
    <td align="right">4.97</td>
    <td align="right">4.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.46</td>
    <td align="right">23.85</td>
    <td align="right">25.03</td>
    <td align="right">23.77</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.98</td>
    <td align="right">28.77</td>
    <td align="right">28.65</td>
    <td align="right">28.65</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.05</td>
    <td align="right">13.15</td>
    <td align="right">13.20</td>
    <td align="right">13.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.02</td>
    <td align="right">35.01</td>
    <td align="right">34.83</td>
    <td align="right">34.93</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.82</td>
    <td align="right">37.88</td>
    <td align="right">37.86</td>
    <td align="right">37.86</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.39</td>
    <td align="right">15.06</td>
    <td align="right">15.15</td>
    <td align="right">15.16</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.14</td>
    <td align="right">2.28</td>
    <td align="right">2.16</td>
    <td align="right">2.16</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.08</td>
    <td align="right">3.47</td>
    <td align="right">3.43</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.18</td>
    <td align="right">3.36</td>
    <td align="right">3.31</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">6.89</td>
    <td align="right">7.40</td>
    <td align="right">6.22</td>
    <td align="right">12.14</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.31</td>
    <td align="right">8.97</td>
    <td align="right">8.03</td>
    <td align="right">14.20</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.87</td>
    <td align="right">8.06</td>
    <td align="right">7.05</td>
    <td align="right">13.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.09</td>
    <td align="right">15.34</td>
    <td align="right">10.92</td>
    <td align="right">17.13</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.57</td>
    <td align="right">19.48</td>
    <td align="right">16.40</td>
    <td align="right">22.76</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.97</td>
    <td align="right">19.05</td>
    <td align="right">16.15</td>
    <td align="right">22.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.73</td>
    <td align="right">17.97</td>
    <td align="right">12.37</td>
    <td align="right">19.91</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.71</td>
    <td align="right">26.97</td>
    <td align="right">19.07</td>
    <td align="right">27.04</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.71</td>
    <td align="right">26.86</td>
    <td align="right">19.08</td>
    <td align="right">26.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.19</td>
    <td align="right">2.24</td>
    <td align="right">2.17</td>
    <td align="right">2.22</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.13</td>
    <td align="right">3.54</td>
    <td align="right">3.45</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.25</td>
    <td align="right">3.40</td>
    <td align="right">3.33</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">6.62</td>
    <td align="right">5.15</td>
    <td align="right">5.02</td>
    <td align="right">4.99</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">7.35</td>
    <td align="right">7.60</td>
    <td align="right">7.37</td>
    <td align="right">7.39</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.73</td>
    <td align="right">10.59</td>
    <td align="right">10.33</td>
    <td align="right">10.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.09</td>
    <td align="right">13.08</td>
    <td align="right">13.10</td>
    <td align="right">13.10</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.12</td>
    <td align="right">19.24</td>
    <td align="right">19.27</td>
    <td align="right">19.31</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.04</td>
    <td align="right">19.24</td>
    <td align="right">19.29</td>
    <td align="right">19.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.73</td>
    <td align="right">15.02</td>
    <td align="right">15.05</td>
    <td align="right">15.04</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.66</td>
    <td align="right">27.66</td>
    <td align="right">27.58</td>
    <td align="right">27.67</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.78</td>
    <td align="right">27.41</td>
    <td align="right">27.52</td>
    <td align="right">27.55</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.70</td>
    <td align="right">7.52</td>
    <td align="right">11.73</td>
    <td align="right">11.64</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.62</td>
    <td align="right">9.66</td>
    <td align="right">14.85</td>
    <td align="right">13.98</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.47</td>
    <td align="right">13.74</td>
    <td align="right">17.31</td>
    <td align="right">16.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">13.60</td>
    <td align="right">14.46</td>
    <td align="right">14.92</td>
    <td align="right">17.23</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">18.43</td>
    <td align="right">17.91</td>
    <td align="right">16.63</td>
    <td align="right">20.27</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">20.53</td>
    <td align="right">22.50</td>
    <td align="right">18.75</td>
    <td align="right">22.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.61</td>
    <td align="right">25.82</td>
    <td align="right">19.77</td>
    <td align="right">27.21</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.54</td>
    <td align="right">32.75</td>
    <td align="right">19.94</td>
    <td align="right">32.63</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">41.13</td>
    <td align="right">43.36</td>
    <td align="right">27.75</td>
    <td align="right">38.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.39</td>
    <td align="right">34.92</td>
    <td align="right">23.01</td>
    <td align="right">37.00</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.85</td>
    <td align="right">41.52</td>
    <td align="right">22.18</td>
    <td align="right">41.86</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.75</td>
    <td align="right">65.32</td>
    <td align="right">37.02</td>
    <td align="right">55.07</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.76</td>
    <td align="right">6.53</td>
    <td align="right">6.55</td>
    <td align="right">6.51</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.48</td>
    <td align="right">8.04</td>
    <td align="right">8.05</td>
    <td align="right">8.01</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.54</td>
    <td align="right">9.96</td>
    <td align="right">10.01</td>
    <td align="right">9.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">13.40</td>
    <td align="right">11.50</td>
    <td align="right">11.17</td>
    <td align="right">11.24</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">18.99</td>
    <td align="right">14.82</td>
    <td align="right">14.38</td>
    <td align="right">14.40</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">16.88</td>
    <td align="right">16.09</td>
    <td align="right">16.05</td>
    <td align="right">16.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.46</td>
    <td align="right">24.16</td>
    <td align="right">24.29</td>
    <td align="right">24.32</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.39</td>
    <td align="right">32.05</td>
    <td align="right">32.09</td>
    <td align="right">32.05</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">42.40</td>
    <td align="right">40.26</td>
    <td align="right">40.18</td>
    <td align="right">40.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.33</td>
    <td align="right">33.35</td>
    <td align="right">33.52</td>
    <td align="right">33.43</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.64</td>
    <td align="right">40.36</td>
    <td align="right">40.47</td>
    <td align="right">40.62</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.78</td>
    <td align="right">64.59</td>
    <td align="right">64.69</td>
    <td align="right">64.62</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">73.65</td>
    <td align="right">34.18</td>
    <td align="right">14.53</td>
    <td align="right">29.07</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">31.00</td>
    <td align="right">44.54</td>
    <td align="right">37.47</td>
    <td align="right">40.67</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.22</td>
    <td align="right">16.12</td>
    <td align="right">16.15</td>
    <td align="right">16.17</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.60</td>
    <td align="right">17.57</td>
    <td align="right">18.09</td>
    <td align="right">18.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.60</td>
    <td align="right">67.00</td>
    <td align="right">40.51</td>
    <td align="right">53.66</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.38</td>
    <td align="right">18.42</td>
    <td align="right">18.47</td>
    <td align="right">18.54</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.05</td>
    <td align="right">19.05</td>
    <td align="right">18.99</td>
    <td align="right">19.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.82</td>
    <td align="right">82.15</td>
    <td align="right">38.87</td>
    <td align="right">61.46</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.36</td>
    <td align="right">20.50</td>
    <td align="right">20.45</td>
    <td align="right">20.46</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.92</td>
    <td align="right">21.70</td>
    <td align="right">21.13</td>
    <td align="right">20.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.74</td>
    <td align="right">104.40</td>
    <td align="right">40.66</td>
    <td align="right">71.74</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">22.16</td>
    <td align="right">22.16</td>
    <td align="right">22.16</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.69</td>
    <td align="right">23.01</td>
    <td align="right">22.01</td>
    <td align="right">21.99</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.63</td>
    <td align="right">40.85</td>
    <td align="right">40.85</td>
    <td align="right">40.90</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.34</td>
    <td align="right">16.26</td>
    <td align="right">16.24</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.58</td>
    <td align="right">18.03</td>
    <td align="right">17.67</td>
    <td align="right">18.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.88</td>
    <td align="right">60.88</td>
    <td align="right">60.91</td>
    <td align="right">61.07</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.28</td>
    <td align="right">18.38</td>
    <td align="right">18.40</td>
    <td align="right">18.24</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.05</td>
    <td align="right">19.29</td>
    <td align="right">19.02</td>
    <td align="right">19.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.78</td>
    <td align="right">70.99</td>
    <td align="right">70.90</td>
    <td align="right">71.31</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.37</td>
    <td align="right">20.51</td>
    <td align="right">20.49</td>
    <td align="right">20.50</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.91</td>
    <td align="right">20.99</td>
    <td align="right">20.98</td>
    <td align="right">21.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.65</td>
    <td align="right">112.87</td>
    <td align="right">112.93</td>
    <td align="right">112.95</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.65</td>
    <td align="right">22.17</td>
    <td align="right">22.17</td>
    <td align="right">22.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.13</td>
    <td align="right">23.10</td>
    <td align="right">23.02</td>
    <td align="right">22.01</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">20.51</td>
    <td align="right">23.90</td>
    <td align="right">26.83</td>
    <td align="right">27.70</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">27.99</td>
    <td align="right">29.26</td>
    <td align="right">30.65</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.83</td>
    <td align="right">14.96</td>
    <td align="right">24.00</td>
    <td align="right">21.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.72</td>
    <td align="right">30.69</td>
    <td align="right">28.65</td>
    <td align="right">31.86</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.04</td>
    <td align="right">34.48</td>
    <td align="right">34.23</td>
    <td align="right">35.59</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.96</td>
    <td align="right">17.59</td>
    <td align="right">25.42</td>
    <td align="right">22.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.31</td>
    <td align="right">44.10</td>
    <td align="right">30.51</td>
    <td align="right">40.77</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.83</td>
    <td align="right">49.24</td>
    <td align="right">40.02</td>
    <td align="right">44.66</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.03</td>
    <td align="right">20.14</td>
    <td align="right">26.35</td>
    <td align="right">25.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.48</td>
    <td align="right">47.26</td>
    <td align="right">29.62</td>
    <td align="right">41.68</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.17</td>
    <td align="right">56.85</td>
    <td align="right">41.86</td>
    <td align="right">49.52</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.98</td>
    <td align="right">27.83</td>
    <td align="right">25.85</td>
    <td align="right">30.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.84</td>
    <td align="right">23.74</td>
    <td align="right">23.72</td>
    <td align="right">23.72</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.20</td>
    <td align="right">26.50</td>
    <td align="right">26.48</td>
    <td align="right">26.49</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.76</td>
    <td align="right">15.64</td>
    <td align="right">15.56</td>
    <td align="right">15.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">27.06</td>
    <td align="right">30.43</td>
    <td align="right">30.01</td>
    <td align="right">30.01</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">34.58</td>
    <td align="right">34.58</td>
    <td align="right">34.58</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.94</td>
    <td align="right">17.78</td>
    <td align="right">17.77</td>
    <td align="right">17.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.44</td>
    <td align="right">36.96</td>
    <td align="right">37.08</td>
    <td align="right">37.00</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.87</td>
    <td align="right">48.99</td>
    <td align="right">49.04</td>
    <td align="right">48.95</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.06</td>
    <td align="right">20.83</td>
    <td align="right">20.84</td>
    <td align="right">20.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.36</td>
    <td align="right">41.57</td>
    <td align="right">41.77</td>
    <td align="right">41.71</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.26</td>
    <td align="right">58.47</td>
    <td align="right">58.56</td>
    <td align="right">58.60</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">23.96</td>
    <td align="right">26.10</td>
    <td align="right">26.10</td>
    <td align="right">26.02</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.41</td>
    <td align="right">16.51</td>
    <td align="right">25.96</td>
    <td align="right">23.77</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">20.61</td>
    <td align="right">23.91</td>
    <td align="right">26.86</td>
    <td align="right">27.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">27.56</td>
    <td align="right">29.28</td>
    <td align="right">30.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.00</td>
    <td align="right">19.85</td>
    <td align="right">26.88</td>
    <td align="right">25.84</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.54</td>
    <td align="right">30.73</td>
    <td align="right">28.48</td>
    <td align="right">32.19</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.03</td>
    <td align="right">34.50</td>
    <td align="right">34.26</td>
    <td align="right">35.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.46</td>
    <td align="right">23.01</td>
    <td align="right">28.24</td>
    <td align="right">28.64</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.43</td>
    <td align="right">43.35</td>
    <td align="right">30.49</td>
    <td align="right">39.50</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.88</td>
    <td align="right">49.26</td>
    <td align="right">40.02</td>
    <td align="right">44.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.76</td>
    <td align="right">30.62</td>
    <td align="right">28.96</td>
    <td align="right">32.64</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.61</td>
    <td align="right">48.79</td>
    <td align="right">29.59</td>
    <td align="right">42.05</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.57</td>
    <td align="right">57.02</td>
    <td align="right">41.95</td>
    <td align="right">49.70</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.64</td>
    <td align="right">16.86</td>
    <td align="right">16.86</td>
    <td align="right">16.85</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.93</td>
    <td align="right">23.73</td>
    <td align="right">23.76</td>
    <td align="right">23.72</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.20</td>
    <td align="right">26.49</td>
    <td align="right">26.49</td>
    <td align="right">26.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.01</td>
    <td align="right">21.05</td>
    <td align="right">21.34</td>
    <td align="right">21.07</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.58</td>
    <td align="right">30.04</td>
    <td align="right">30.12</td>
    <td align="right">30.31</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">34.59</td>
    <td align="right">34.59</td>
    <td align="right">34.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.43</td>
    <td align="right">25.09</td>
    <td align="right">25.08</td>
    <td align="right">25.09</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.10</td>
    <td align="right">36.86</td>
    <td align="right">36.90</td>
    <td align="right">36.97</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.79</td>
    <td align="right">49.00</td>
    <td align="right">49.08</td>
    <td align="right">48.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.68</td>
    <td align="right">33.10</td>
    <td align="right">33.10</td>
    <td align="right">33.10</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.38</td>
    <td align="right">41.59</td>
    <td align="right">41.55</td>
    <td align="right">41.66</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.55</td>
    <td align="right">58.46</td>
    <td align="right">58.42</td>
    <td align="right">58.47</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.33</td>
    <td align="right">24.47</td>
    <td align="right">27.81</td>
    <td align="right">28.18</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.67</td>
    <td align="right">31.52</td>
    <td align="right">35.55</td>
    <td align="right">33.70</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.17</td>
    <td align="right">36.64</td>
    <td align="right">33.60</td>
    <td align="right">34.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.28</td>
    <td align="right">37.07</td>
    <td align="right">28.60</td>
    <td align="right">35.94</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.28</td>
    <td align="right">40.72</td>
    <td align="right">34.71</td>
    <td align="right">39.24</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.14</td>
    <td align="right">47.12</td>
    <td align="right">35.00</td>
    <td align="right">41.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.13</td>
    <td align="right">43.86</td>
    <td align="right">27.93</td>
    <td align="right">39.80</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.50</td>
    <td align="right">49.70</td>
    <td align="right">36.11</td>
    <td align="right">44.30</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.06</td>
    <td align="right">50.23</td>
    <td align="right">32.31</td>
    <td align="right">43.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.26</td>
    <td align="right">49.14</td>
    <td align="right">29.31</td>
    <td align="right">42.51</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.34</td>
    <td align="right">53.08</td>
    <td align="right">35.95</td>
    <td align="right">46.60</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.61</td>
    <td align="right">65.35</td>
    <td align="right">36.51</td>
    <td align="right">52.34</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.32</td>
    <td align="right">24.21</td>
    <td align="right">24.17</td>
    <td align="right">24.36</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.70</td>
    <td align="right">32.59</td>
    <td align="right">32.62</td>
    <td align="right">32.62</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.31</td>
    <td align="right">34.75</td>
    <td align="right">34.64</td>
    <td align="right">34.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.35</td>
    <td align="right">33.64</td>
    <td align="right">33.64</td>
    <td align="right">33.66</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">44.94</td>
    <td align="right">39.38</td>
    <td align="right">39.36</td>
    <td align="right">39.36</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.61</td>
    <td align="right">44.73</td>
    <td align="right">44.53</td>
    <td align="right">44.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.11</td>
    <td align="right">41.15</td>
    <td align="right">41.18</td>
    <td align="right">41.12</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.49</td>
    <td align="right">48.21</td>
    <td align="right">48.21</td>
    <td align="right">48.22</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">45.07</td>
    <td align="right">47.55</td>
    <td align="right">47.09</td>
    <td align="right">47.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.26</td>
    <td align="right">46.93</td>
    <td align="right">46.70</td>
    <td align="right">46.88</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.35</td>
    <td align="right">52.41</td>
    <td align="right">52.40</td>
    <td align="right">52.41</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">60.14</td>
    <td align="right">65.03</td>
    <td align="right">64.69</td>
    <td align="right">64.78</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.04</td>
    <td align="right">126.00</td>
    <td align="right">27.56</td>
    <td align="right">83.24</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">38.14</td>
    <td align="right">53.78</td>
    <td align="right">44.36</td>
    <td align="right">49.04</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.43</td>
    <td align="right">17.28</td>
    <td align="right">17.33</td>
    <td align="right">17.30</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.70</td>
    <td align="right">20.85</td>
    <td align="right">20.85</td>
    <td align="right">20.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">100.47</td>
    <td align="right">130.76</td>
    <td align="right">60.13</td>
    <td align="right">95.42</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.32</td>
    <td align="right">28.79</td>
    <td align="right">28.68</td>
    <td align="right">28.86</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.31</td>
    <td align="right">29.04</td>
    <td align="right">28.96</td>
    <td align="right">28.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.79</td>
    <td align="right">242.04</td>
    <td align="right">76.14</td>
    <td align="right">159.89</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.12</td>
    <td align="right">48.43</td>
    <td align="right">48.40</td>
    <td align="right">48.40</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.28</td>
    <td align="right">49.24</td>
    <td align="right">49.30</td>
    <td align="right">49.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">295.82</td>
    <td align="right">399.44</td>
    <td align="right">103.40</td>
    <td align="right">271.62</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.75</td>
    <td align="right">62.19</td>
    <td align="right">62.20</td>
    <td align="right">62.20</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">56.33</td>
    <td align="right">63.42</td>
    <td align="right">63.43</td>
    <td align="right">63.23</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">33.33</td>
    <td align="right">42.75</td>
    <td align="right">42.74</td>
    <td align="right">42.73</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.66</td>
    <td align="right">17.49</td>
    <td align="right">17.60</td>
    <td align="right">17.65</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.60</td>
    <td align="right">21.17</td>
    <td align="right">21.00</td>
    <td align="right">20.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">98.80</td>
    <td align="right">109.65</td>
    <td align="right">107.42</td>
    <td align="right">107.01</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.42</td>
    <td align="right">28.59</td>
    <td align="right">28.43</td>
    <td align="right">28.22</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">25.62</td>
    <td align="right">31.21</td>
    <td align="right">31.13</td>
    <td align="right">31.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">186.96</td>
    <td align="right">175.81</td>
    <td align="right">175.20</td>
    <td align="right">175.74</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.25</td>
    <td align="right">47.95</td>
    <td align="right">47.95</td>
    <td align="right">47.94</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.76</td>
    <td align="right">49.69</td>
    <td align="right">49.72</td>
    <td align="right">49.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.96</td>
    <td align="right">414.74</td>
    <td align="right">415.26</td>
    <td align="right">416.78</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.01</td>
    <td align="right">62.53</td>
    <td align="right">62.61</td>
    <td align="right">62.54</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">52.61</td>
    <td align="right">65.65</td>
    <td align="right">67.34</td>
    <td align="right">67.34</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.31</td>
    <td align="right">27.76</td>
    <td align="right">29.97</td>
    <td align="right">32.64</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.86</td>
    <td align="right">33.78</td>
    <td align="right">32.01</td>
    <td align="right">36.73</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.06</td>
    <td align="right">17.65</td>
    <td align="right">26.20</td>
    <td align="right">24.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.08</td>
    <td align="right">41.70</td>
    <td align="right">35.95</td>
    <td align="right">42.71</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.62</td>
    <td align="right">52.19</td>
    <td align="right">45.79</td>
    <td align="right">52.18</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.27</td>
    <td align="right">27.71</td>
    <td align="right">34.54</td>
    <td align="right">33.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.29</td>
    <td align="right">76.08</td>
    <td align="right">48.81</td>
    <td align="right">68.93</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.82</td>
    <td align="right">84.51</td>
    <td align="right">68.13</td>
    <td align="right">78.89</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.42</td>
    <td align="right">43.91</td>
    <td align="right">43.95</td>
    <td align="right">46.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.27</td>
    <td align="right">98.17</td>
    <td align="right">56.35</td>
    <td align="right">89.58</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.44</td>
    <td align="right">109.42</td>
    <td align="right">88.27</td>
    <td align="right">99.76</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.78</td>
    <td align="right">75.49</td>
    <td align="right">49.63</td>
    <td align="right">72.88</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.39</td>
    <td align="right">27.54</td>
    <td align="right">27.48</td>
    <td align="right">27.53</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.03</td>
    <td align="right">31.54</td>
    <td align="right">31.57</td>
    <td align="right">31.70</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">16.02</td>
    <td align="right">19.00</td>
    <td align="right">19.05</td>
    <td align="right">19.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.37</td>
    <td align="right">44.81</td>
    <td align="right">44.85</td>
    <td align="right">44.79</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.36</td>
    <td align="right">48.70</td>
    <td align="right">48.64</td>
    <td align="right">48.74</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">26.35</td>
    <td align="right">28.63</td>
    <td align="right">29.16</td>
    <td align="right">29.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.80</td>
    <td align="right">71.25</td>
    <td align="right">71.29</td>
    <td align="right">71.29</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.05</td>
    <td align="right">83.32</td>
    <td align="right">83.45</td>
    <td align="right">83.37</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">41.91</td>
    <td align="right">45.10</td>
    <td align="right">45.05</td>
    <td align="right">45.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.32</td>
    <td align="right">94.74</td>
    <td align="right">96.43</td>
    <td align="right">94.71</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.11</td>
    <td align="right">109.39</td>
    <td align="right">109.28</td>
    <td align="right">109.39</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.34</td>
    <td align="right">76.37</td>
    <td align="right">76.07</td>
    <td align="right">76.08</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.44</td>
    <td align="right">18.94</td>
    <td align="right">29.14</td>
    <td align="right">26.86</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">25.27</td>
    <td align="right">29.07</td>
    <td align="right">30.96</td>
    <td align="right">33.75</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.17</td>
    <td align="right">34.10</td>
    <td align="right">32.46</td>
    <td align="right">37.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.84</td>
    <td align="right">31.76</td>
    <td align="right">37.97</td>
    <td align="right">37.45</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.75</td>
    <td align="right">42.70</td>
    <td align="right">36.60</td>
    <td align="right">44.11</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">56.78</td>
    <td align="right">51.60</td>
    <td align="right">46.44</td>
    <td align="right">51.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.73</td>
    <td align="right">48.52</td>
    <td align="right">51.52</td>
    <td align="right">51.56</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.75</td>
    <td align="right">76.51</td>
    <td align="right">49.09</td>
    <td align="right">70.12</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.71</td>
    <td align="right">82.83</td>
    <td align="right">67.14</td>
    <td align="right">77.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.99</td>
    <td align="right">81.61</td>
    <td align="right">59.83</td>
    <td align="right">79.32</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.32</td>
    <td align="right">97.69</td>
    <td align="right">56.01</td>
    <td align="right">87.99</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.99</td>
    <td align="right">107.68</td>
    <td align="right">86.88</td>
    <td align="right">98.03</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.77</td>
    <td align="right">18.73</td>
    <td align="right">19.18</td>
    <td align="right">18.76</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.75</td>
    <td align="right">27.79</td>
    <td align="right">27.81</td>
    <td align="right">27.71</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">31.75</td>
    <td align="right">33.27</td>
    <td align="right">33.20</td>
    <td align="right">33.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">28.80</td>
    <td align="right">31.74</td>
    <td align="right">31.61</td>
    <td align="right">31.42</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.64</td>
    <td align="right">42.46</td>
    <td align="right">42.52</td>
    <td align="right">42.29</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">56.09</td>
    <td align="right">50.97</td>
    <td align="right">50.93</td>
    <td align="right">50.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.72</td>
    <td align="right">55.99</td>
    <td align="right">59.01</td>
    <td align="right">60.54</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.90</td>
    <td align="right">71.82</td>
    <td align="right">71.93</td>
    <td align="right">71.74</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.51</td>
    <td align="right">86.81</td>
    <td align="right">86.29</td>
    <td align="right">85.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.36</td>
    <td align="right">83.61</td>
    <td align="right">83.74</td>
    <td align="right">83.78</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.28</td>
    <td align="right">92.79</td>
    <td align="right">92.77</td>
    <td align="right">92.81</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.23</td>
    <td align="right">109.59</td>
    <td align="right">109.53</td>
    <td align="right">109.56</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.22</td>
    <td align="right">28.84</td>
    <td align="right">30.79</td>
    <td align="right">33.00</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.94</td>
    <td align="right">37.72</td>
    <td align="right">41.04</td>
    <td align="right">40.09</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.83</td>
    <td align="right">44.07</td>
    <td align="right">40.72</td>
    <td align="right">44.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.22</td>
    <td align="right">51.03</td>
    <td align="right">39.08</td>
    <td align="right">49.71</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.74</td>
    <td align="right">54.33</td>
    <td align="right">44.49</td>
    <td align="right">52.27</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.18</td>
    <td align="right">67.93</td>
    <td align="right">43.58</td>
    <td align="right">57.86</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.26</td>
    <td align="right">72.63</td>
    <td align="right">49.48</td>
    <td align="right">71.44</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.25</td>
    <td align="right">88.24</td>
    <td align="right">60.09</td>
    <td align="right">80.96</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">91.28</td>
    <td align="right">94.57</td>
    <td align="right">44.88</td>
    <td align="right">78.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.81</td>
    <td align="right">89.39</td>
    <td align="right">56.34</td>
    <td align="right">82.41</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.15</td>
    <td align="right">104.44</td>
    <td align="right">67.30</td>
    <td align="right">94.20</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.17</td>
    <td align="right">138.91</td>
    <td align="right">49.74</td>
    <td align="right">108.90</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.55</td>
    <td align="right">28.53</td>
    <td align="right">29.01</td>
    <td align="right">28.57</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">34.89</td>
    <td align="right">35.68</td>
    <td align="right">35.65</td>
    <td align="right">35.66</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">35.85</td>
    <td align="right">41.60</td>
    <td align="right">40.20</td>
    <td align="right">40.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.64</td>
    <td align="right">43.13</td>
    <td align="right">43.14</td>
    <td align="right">43.13</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">61.02</td>
    <td align="right">55.10</td>
    <td align="right">55.02</td>
    <td align="right">54.89</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">66.37</td>
    <td align="right">69.53</td>
    <td align="right">69.54</td>
    <td align="right">69.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.43</td>
    <td align="right">67.96</td>
    <td align="right">67.97</td>
    <td align="right">67.91</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">85.99</td>
    <td align="right">84.80</td>
    <td align="right">84.82</td>
    <td align="right">84.69</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.15</td>
    <td align="right">94.37</td>
    <td align="right">94.48</td>
    <td align="right">94.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.94</td>
    <td align="right">87.67</td>
    <td align="right">87.81</td>
    <td align="right">87.73</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.31</td>
    <td align="right">104.70</td>
    <td align="right">104.72</td>
    <td align="right">104.67</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.70</td>
    <td align="right">139.09</td>
    <td align="right">139.31</td>
    <td align="right">140.37</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.27</td>
    <td align="right">13.88</td>
    <td align="right">8.58</td>
    <td align="right">18.00</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.61</td>
    <td align="right">28.48</td>
    <td align="right">29.23</td>
    <td align="right">29.50</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">13.91</td>
    <td align="right">14.04</td>
    <td align="right">13.92</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">18.01</td>
    <td align="right">18.03</td>
    <td align="right">18.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.61</td>
    <td align="right">42.65</td>
    <td align="right">31.24</td>
    <td align="right">37.66</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.15</td>
    <td align="right">18.42</td>
    <td align="right">18.42</td>
    <td align="right">18.43</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.22</td>
    <td align="right">20.93</td>
    <td align="right">20.73</td>
    <td align="right">20.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.08</td>
    <td align="right">64.92</td>
    <td align="right">32.27</td>
    <td align="right">48.39</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.72</td>
    <td align="right">21.34</td>
    <td align="right">21.18</td>
    <td align="right">21.44</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">21.98</td>
    <td align="right">22.84</td>
    <td align="right">22.92</td>
    <td align="right">22.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">62.86</td>
    <td align="right">80.02</td>
    <td align="right">33.49</td>
    <td align="right">59.10</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.16</td>
    <td align="right">23.19</td>
    <td align="right">23.28</td>
    <td align="right">23.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.78</td>
    <td align="right">25.66</td>
    <td align="right">25.68</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.61</td>
    <td align="right">30.15</td>
    <td align="right">30.04</td>
    <td align="right">30.11</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">13.91</td>
    <td align="right">13.91</td>
    <td align="right">14.06</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.85</td>
    <td align="right">18.03</td>
    <td align="right">18.01</td>
    <td align="right">17.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.67</td>
    <td align="right">46.66</td>
    <td align="right">46.50</td>
    <td align="right">46.65</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.03</td>
    <td align="right">18.40</td>
    <td align="right">18.49</td>
    <td align="right">18.42</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">20.69</td>
    <td align="right">20.79</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.22</td>
    <td align="right">56.75</td>
    <td align="right">57.13</td>
    <td align="right">56.81</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.58</td>
    <td align="right">21.29</td>
    <td align="right">21.35</td>
    <td align="right">21.19</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.03</td>
    <td align="right">22.87</td>
    <td align="right">22.88</td>
    <td align="right">22.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">63.18</td>
    <td align="right">72.54</td>
    <td align="right">72.83</td>
    <td align="right">72.53</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.17</td>
    <td align="right">23.28</td>
    <td align="right">23.18</td>
    <td align="right">23.29</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.04</td>
    <td align="right">25.68</td>
    <td align="right">25.82</td>
    <td align="right">25.70</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">20.10</td>
    <td align="right">23.35</td>
    <td align="right">24.06</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.06</td>
    <td align="right">19.63</td>
    <td align="right">23.00</td>
    <td align="right">23.27</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.98</td>
    <td align="right">9.00</td>
    <td align="right">18.52</td>
    <td align="right">15.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">27.42</td>
    <td align="right">25.11</td>
    <td align="right">28.78</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.59</td>
    <td align="right">27.42</td>
    <td align="right">24.88</td>
    <td align="right">28.65</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.95</td>
    <td align="right">12.94</td>
    <td align="right">20.61</td>
    <td align="right">19.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.14</td>
    <td align="right">37.46</td>
    <td align="right">26.65</td>
    <td align="right">34.28</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.55</td>
    <td align="right">35.95</td>
    <td align="right">25.71</td>
    <td align="right">33.11</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.89</td>
    <td align="right">15.12</td>
    <td align="right">29.54</td>
    <td align="right">21.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">41.34</td>
    <td align="right">25.87</td>
    <td align="right">36.50</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.42</td>
    <td align="right">42.92</td>
    <td align="right">26.47</td>
    <td align="right">36.94</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.10</td>
    <td align="right">19.77</td>
    <td align="right">21.16</td>
    <td align="right">24.44</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.08</td>
    <td align="right">18.32</td>
    <td align="right">18.34</td>
    <td align="right">18.51</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.02</td>
    <td align="right">19.02</td>
    <td align="right">18.87</td>
    <td align="right">18.88</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.96</td>
    <td align="right">8.72</td>
    <td align="right">8.72</td>
    <td align="right">8.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">26.57</td>
    <td align="right">26.56</td>
    <td align="right">26.52</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">26.95</td>
    <td align="right">26.93</td>
    <td align="right">26.97</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.76</td>
    <td align="right">13.74</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.13</td>
    <td align="right">35.31</td>
    <td align="right">35.25</td>
    <td align="right">35.26</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">34.47</td>
    <td align="right">34.50</td>
    <td align="right">34.16</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.86</td>
    <td align="right">17.78</td>
    <td align="right">17.77</td>
    <td align="right">17.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.53</td>
    <td align="right">38.32</td>
    <td align="right">39.09</td>
    <td align="right">38.28</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.46</td>
    <td align="right">41.38</td>
    <td align="right">41.29</td>
    <td align="right">41.17</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.10</td>
    <td align="right">19.73</td>
    <td align="right">19.73</td>
    <td align="right">19.73</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.67</td>
    <td align="right">8.67</td>
    <td align="right">17.90</td>
    <td align="right">15.43</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.05</td>
    <td align="right">20.10</td>
    <td align="right">23.36</td>
    <td align="right">24.08</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.04</td>
    <td align="right">19.69</td>
    <td align="right">23.02</td>
    <td align="right">23.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.80</td>
    <td align="right">13.61</td>
    <td align="right">20.26</td>
    <td align="right">19.61</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.67</td>
    <td align="right">27.44</td>
    <td align="right">25.10</td>
    <td align="right">28.79</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.38</td>
    <td align="right">27.14</td>
    <td align="right">24.68</td>
    <td align="right">28.33</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.21</td>
    <td align="right">16.04</td>
    <td align="right">21.26</td>
    <td align="right">21.94</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.10</td>
    <td align="right">37.66</td>
    <td align="right">26.65</td>
    <td align="right">34.41</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.57</td>
    <td align="right">36.34</td>
    <td align="right">25.73</td>
    <td align="right">33.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.78</td>
    <td align="right">19.21</td>
    <td align="right">20.72</td>
    <td align="right">23.86</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.51</td>
    <td align="right">41.32</td>
    <td align="right">25.87</td>
    <td align="right">36.35</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.43</td>
    <td align="right">42.85</td>
    <td align="right">26.47</td>
    <td align="right">36.93</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.68</td>
    <td align="right">8.48</td>
    <td align="right">8.49</td>
    <td align="right">8.48</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">18.45</td>
    <td align="right">18.44</td>
    <td align="right">18.43</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.01</td>
    <td align="right">18.83</td>
    <td align="right">18.83</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.91</td>
    <td align="right">14.10</td>
    <td align="right">14.16</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.66</td>
    <td align="right">26.58</td>
    <td align="right">26.58</td>
    <td align="right">26.54</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.58</td>
    <td align="right">26.98</td>
    <td align="right">26.96</td>
    <td align="right">26.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.27</td>
    <td align="right">17.22</td>
    <td align="right">17.21</td>
    <td align="right">17.21</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.13</td>
    <td align="right">35.29</td>
    <td align="right">35.40</td>
    <td align="right">35.36</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.55</td>
    <td align="right">34.48</td>
    <td align="right">34.50</td>
    <td align="right">34.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.81</td>
    <td align="right">19.98</td>
    <td align="right">19.98</td>
    <td align="right">19.98</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.52</td>
    <td align="right">38.74</td>
    <td align="right">38.23</td>
    <td align="right">38.21</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.41</td>
    <td align="right">41.63</td>
    <td align="right">41.21</td>
    <td align="right">40.97</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.25</td>
    <td align="right">20.98</td>
    <td align="right">24.59</td>
    <td align="right">25.01</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">48.32</td>
    <td align="right">42.00</td>
    <td align="right">41.83</td>
    <td align="right">41.85</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.88</td>
    <td align="right">29.38</td>
    <td align="right">29.08</td>
    <td align="right">29.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.00</td>
    <td align="right">29.36</td>
    <td align="right">24.67</td>
    <td align="right">29.84</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">53.55</td>
    <td align="right">46.07</td>
    <td align="right">39.32</td>
    <td align="right">43.28</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.69</td>
    <td align="right">39.21</td>
    <td align="right">30.11</td>
    <td align="right">35.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.11</td>
    <td align="right">35.44</td>
    <td align="right">24.61</td>
    <td align="right">33.22</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.37</td>
    <td align="right">53.90</td>
    <td align="right">40.29</td>
    <td align="right">47.30</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.56</td>
    <td align="right">45.30</td>
    <td align="right">31.47</td>
    <td align="right">40.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.72</td>
    <td align="right">46.72</td>
    <td align="right">29.81</td>
    <td align="right">41.36</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">64.68</td>
    <td align="right">58.08</td>
    <td align="right">45.17</td>
    <td align="right">51.60</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.20</td>
    <td align="right">57.81</td>
    <td align="right">33.02</td>
    <td align="right">47.06</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.25</td>
    <td align="right">20.01</td>
    <td align="right">20.04</td>
    <td align="right">20.04</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">50.36</td>
    <td align="right">38.03</td>
    <td align="right">38.12</td>
    <td align="right">37.61</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.98</td>
    <td align="right">27.32</td>
    <td align="right">27.11</td>
    <td align="right">27.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">28.39</td>
    <td align="right">28.41</td>
    <td align="right">28.43</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.72</td>
    <td align="right">43.97</td>
    <td align="right">44.67</td>
    <td align="right">44.38</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.56</td>
    <td align="right">36.51</td>
    <td align="right">36.47</td>
    <td align="right">36.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.12</td>
    <td align="right">34.29</td>
    <td align="right">34.30</td>
    <td align="right">34.28</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">61.28</td>
    <td align="right">48.70</td>
    <td align="right">48.67</td>
    <td align="right">48.50</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.68</td>
    <td align="right">38.80</td>
    <td align="right">38.81</td>
    <td align="right">38.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.73</td>
    <td align="right">39.31</td>
    <td align="right">39.28</td>
    <td align="right">39.29</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.70</td>
    <td align="right">52.64</td>
    <td align="right">52.51</td>
    <td align="right">52.68</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.32</td>
    <td align="right">50.67</td>
    <td align="right">50.45</td>
    <td align="right">50.48</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.04</td>
    <td align="right">61.98</td>
    <td align="right">23.10</td>
    <td align="right">53.38</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">27.27</td>
    <td align="right">35.19</td>
    <td align="right">34.29</td>
    <td align="right">35.82</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.65</td>
    <td align="right">16.23</td>
    <td align="right">16.15</td>
    <td align="right">16.13</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.92</td>
    <td align="right">21.04</td>
    <td align="right">21.03</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">79.86</td>
    <td align="right">98.01</td>
    <td align="right">47.41</td>
    <td align="right">73.75</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.30</td>
    <td align="right">26.54</td>
    <td align="right">26.51</td>
    <td align="right">26.46</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.67</td>
    <td align="right">35.41</td>
    <td align="right">35.30</td>
    <td align="right">35.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.88</td>
    <td align="right">206.50</td>
    <td align="right">66.67</td>
    <td align="right">132.61</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.61</td>
    <td align="right">49.13</td>
    <td align="right">49.19</td>
    <td align="right">49.16</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">50.85</td>
    <td align="right">51.11</td>
    <td align="right">51.19</td>
    <td align="right">51.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.23</td>
    <td align="right">328.11</td>
    <td align="right">83.39</td>
    <td align="right">192.56</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">63.92</td>
    <td align="right">64.63</td>
    <td align="right">64.86</td>
    <td align="right">64.80</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.64</td>
    <td align="right">69.04</td>
    <td align="right">68.99</td>
    <td align="right">69.05</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">23.00</td>
    <td align="right">32.62</td>
    <td align="right">33.19</td>
    <td align="right">32.61</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">14.93</td>
    <td align="right">16.39</td>
    <td align="right">16.44</td>
    <td align="right">16.45</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.38</td>
    <td align="right">20.46</td>
    <td align="right">20.48</td>
    <td align="right">20.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">74.71</td>
    <td align="right">90.91</td>
    <td align="right">90.19</td>
    <td align="right">90.49</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">26.11</td>
    <td align="right">28.16</td>
    <td align="right">28.33</td>
    <td align="right">28.36</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">29.39</td>
    <td align="right">32.66</td>
    <td align="right">32.57</td>
    <td align="right">32.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">145.10</td>
    <td align="right">191.47</td>
    <td align="right">191.32</td>
    <td align="right">191.24</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.09</td>
    <td align="right">48.58</td>
    <td align="right">48.40</td>
    <td align="right">48.41</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.83</td>
    <td align="right">50.66</td>
    <td align="right">50.68</td>
    <td align="right">50.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.30</td>
    <td align="right">288.03</td>
    <td align="right">288.12</td>
    <td align="right">290.29</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.00</td>
    <td align="right">64.90</td>
    <td align="right">64.78</td>
    <td align="right">64.82</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.45</td>
    <td align="right">67.21</td>
    <td align="right">67.25</td>
    <td align="right">67.23</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">18.55</td>
    <td align="right">21.98</td>
    <td align="right">24.76</td>
    <td align="right">27.22</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.08</td>
    <td align="right">21.18</td>
    <td align="right">24.38</td>
    <td align="right">25.89</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.76</td>
    <td align="right">11.69</td>
    <td align="right">20.96</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.58</td>
    <td align="right">42.00</td>
    <td align="right">33.89</td>
    <td align="right">43.53</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.12</td>
    <td align="right">40.30</td>
    <td align="right">31.86</td>
    <td align="right">40.59</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.26</td>
    <td align="right">21.78</td>
    <td align="right">27.37</td>
    <td align="right">27.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.30</td>
    <td align="right">68.69</td>
    <td align="right">41.89</td>
    <td align="right">62.10</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">72.13</td>
    <td align="right">72.57</td>
    <td align="right">44.04</td>
    <td align="right">66.30</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.24</td>
    <td align="right">37.91</td>
    <td align="right">55.49</td>
    <td align="right">40.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.27</td>
    <td align="right">89.86</td>
    <td align="right">47.16</td>
    <td align="right">79.98</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.32</td>
    <td align="right">92.52</td>
    <td align="right">49.67</td>
    <td align="right">82.03</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.19</td>
    <td align="right">51.84</td>
    <td align="right">38.92</td>
    <td align="right">52.28</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.00</td>
    <td align="right">22.47</td>
    <td align="right">22.48</td>
    <td align="right">22.59</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.38</td>
    <td align="right">23.16</td>
    <td align="right">23.24</td>
    <td align="right">22.96</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.27</td>
    <td align="right">11.07</td>
    <td align="right">11.20</td>
    <td align="right">11.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.06</td>
    <td align="right">39.79</td>
    <td align="right">39.78</td>
    <td align="right">39.65</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.45</td>
    <td align="right">45.37</td>
    <td align="right">45.43</td>
    <td align="right">45.41</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.00</td>
    <td align="right">23.37</td>
    <td align="right">23.87</td>
    <td align="right">23.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.75</td>
    <td align="right">67.11</td>
    <td align="right">67.21</td>
    <td align="right">67.04</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.13</td>
    <td align="right">68.77</td>
    <td align="right">68.49</td>
    <td align="right">68.78</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.37</td>
    <td align="right">41.26</td>
    <td align="right">41.21</td>
    <td align="right">42.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.81</td>
    <td align="right">86.44</td>
    <td align="right">87.26</td>
    <td align="right">86.47</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.69</td>
    <td align="right">94.93</td>
    <td align="right">93.86</td>
    <td align="right">93.53</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.97</td>
    <td align="right">52.33</td>
    <td align="right">52.37</td>
    <td align="right">52.33</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.41</td>
    <td align="right">9.72</td>
    <td align="right">19.39</td>
    <td align="right">17.10</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.71</td>
    <td align="right">23.63</td>
    <td align="right">25.52</td>
    <td align="right">29.01</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.92</td>
    <td align="right">22.89</td>
    <td align="right">25.47</td>
    <td align="right">27.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.15</td>
    <td align="right">24.37</td>
    <td align="right">27.41</td>
    <td align="right">29.17</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.01</td>
    <td align="right">41.48</td>
    <td align="right">33.40</td>
    <td align="right">42.93</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">42.31</td>
    <td align="right">40.91</td>
    <td align="right">32.01</td>
    <td align="right">41.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.70</td>
    <td align="right">39.64</td>
    <td align="right">33.83</td>
    <td align="right">40.54</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.07</td>
    <td align="right">68.89</td>
    <td align="right">41.97</td>
    <td align="right">62.63</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.96</td>
    <td align="right">69.84</td>
    <td align="right">43.01</td>
    <td align="right">64.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.06</td>
    <td align="right">53.04</td>
    <td align="right">38.21</td>
    <td align="right">53.22</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.04</td>
    <td align="right">91.69</td>
    <td align="right">47.69</td>
    <td align="right">81.64</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.48</td>
    <td align="right">94.99</td>
    <td align="right">50.59</td>
    <td align="right">84.37</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.50</td>
    <td align="right">11.21</td>
    <td align="right">11.13</td>
    <td align="right">11.09</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.37</td>
    <td align="right">21.08</td>
    <td align="right">21.19</td>
    <td align="right">21.28</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.34</td>
    <td align="right">22.91</td>
    <td align="right">22.96</td>
    <td align="right">23.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.40</td>
    <td align="right">25.93</td>
    <td align="right">25.79</td>
    <td align="right">25.73</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.06</td>
    <td align="right">41.66</td>
    <td align="right">41.64</td>
    <td align="right">41.54</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.38</td>
    <td align="right">42.68</td>
    <td align="right">42.70</td>
    <td align="right">42.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.75</td>
    <td align="right">40.13</td>
    <td align="right">40.32</td>
    <td align="right">40.31</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.80</td>
    <td align="right">68.39</td>
    <td align="right">68.48</td>
    <td align="right">68.43</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.48</td>
    <td align="right">66.71</td>
    <td align="right">66.64</td>
    <td align="right">66.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.07</td>
    <td align="right">53.64</td>
    <td align="right">53.63</td>
    <td align="right">53.61</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.74</td>
    <td align="right">85.93</td>
    <td align="right">85.95</td>
    <td align="right">85.97</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.16</td>
    <td align="right">93.48</td>
    <td align="right">92.92</td>
    <td align="right">92.16</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">19.85</td>
    <td align="right">22.97</td>
    <td align="right">25.96</td>
    <td align="right">28.13</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">50.00</td>
    <td align="right">43.92</td>
    <td align="right">43.76</td>
    <td align="right">43.52</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.57</td>
    <td align="right">38.29</td>
    <td align="right">33.49</td>
    <td align="right">37.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.97</td>
    <td align="right">43.24</td>
    <td align="right">32.08</td>
    <td align="right">43.74</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">64.66</td>
    <td align="right">57.23</td>
    <td align="right">48.16</td>
    <td align="right">55.46</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">63.32</td>
    <td align="right">59.26</td>
    <td align="right">37.58</td>
    <td align="right">51.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.78</td>
    <td align="right">63.78</td>
    <td align="right">40.82</td>
    <td align="right">61.20</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.28</td>
    <td align="right">86.18</td>
    <td align="right">63.11</td>
    <td align="right">78.79</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.92</td>
    <td align="right">91.52</td>
    <td align="right">43.06</td>
    <td align="right">76.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.41</td>
    <td align="right">87.15</td>
    <td align="right">55.98</td>
    <td align="right">81.40</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.94</td>
    <td align="right">104.52</td>
    <td align="right">78.28</td>
    <td align="right">95.10</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">132.75</td>
    <td align="right">133.94</td>
    <td align="right">49.13</td>
    <td align="right">104.99</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.26</td>
    <td align="right">23.48</td>
    <td align="right">23.48</td>
    <td align="right">23.51</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">52.46</td>
    <td align="right">40.35</td>
    <td align="right">40.45</td>
    <td align="right">39.99</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.59</td>
    <td align="right">36.45</td>
    <td align="right">37.50</td>
    <td align="right">36.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">38.97</td>
    <td align="right">40.41</td>
    <td align="right">40.34</td>
    <td align="right">40.38</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">65.48</td>
    <td align="right">57.36</td>
    <td align="right">59.70</td>
    <td align="right">57.50</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">58.95</td>
    <td align="right">51.62</td>
    <td align="right">51.67</td>
    <td align="right">51.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">61.56</td>
    <td align="right">60.18</td>
    <td align="right">60.15</td>
    <td align="right">60.20</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">90.18</td>
    <td align="right">81.86</td>
    <td align="right">80.51</td>
    <td align="right">82.74</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">85.38</td>
    <td align="right">81.74</td>
    <td align="right">81.76</td>
    <td align="right">81.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.28</td>
    <td align="right">80.87</td>
    <td align="right">80.81</td>
    <td align="right">80.91</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">108.41</td>
    <td align="right">96.98</td>
    <td align="right">97.01</td>
    <td align="right">97.06</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.20</td>
    <td align="right">118.07</td>
    <td align="right">117.97</td>
    <td align="right">118.16</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.92</td>
    <td align="right">6.67</td>
    <td align="right">5.91</td>
    <td align="right">11.95</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.10</td>
    <td align="right">60.59</td>
    <td align="right">41.16</td>
    <td align="right">50.18</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.00</td>
    <td align="right">20.67</td>
    <td align="right">22.91</td>
    <td align="right">24.89</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">25.16</td>
    <td align="right">25.32</td>
    <td align="right">26.22</td>
    <td align="right">28.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">98.77</td>
    <td align="right">87.23</td>
    <td align="right">41.47</td>
    <td align="right">64.67</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.21</td>
    <td align="right">22.11</td>
    <td align="right">24.09</td>
    <td align="right">26.65</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.46</td>
    <td align="right">27.79</td>
    <td align="right">28.56</td>
    <td align="right">30.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">122.60</td>
    <td align="right">105.78</td>
    <td align="right">40.99</td>
    <td align="right">72.04</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.15</td>
    <td align="right">25.81</td>
    <td align="right">25.91</td>
    <td align="right">28.77</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.03</td>
    <td align="right">29.89</td>
    <td align="right">30.08</td>
    <td align="right">32.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">158.66</td>
    <td align="right">137.13</td>
    <td align="right">41.59</td>
    <td align="right">88.97</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.49</td>
    <td align="right">26.68</td>
    <td align="right">27.12</td>
    <td align="right">30.40</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">30.84</td>
    <td align="right">31.56</td>
    <td align="right">32.17</td>
    <td align="right">36.16</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.98</td>
    <td align="right">62.81</td>
    <td align="right">63.22</td>
    <td align="right">62.71</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.88</td>
    <td align="right">20.56</td>
    <td align="right">22.75</td>
    <td align="right">24.87</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.95</td>
    <td align="right">25.06</td>
    <td align="right">26.54</td>
    <td align="right">27.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">103.54</td>
    <td align="right">91.09</td>
    <td align="right">90.99</td>
    <td align="right">89.96</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.48</td>
    <td align="right">22.48</td>
    <td align="right">24.41</td>
    <td align="right">27.65</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.51</td>
    <td align="right">27.95</td>
    <td align="right">28.62</td>
    <td align="right">31.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">131.19</td>
    <td align="right">109.40</td>
    <td align="right">109.50</td>
    <td align="right">108.75</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.29</td>
    <td align="right">25.88</td>
    <td align="right">25.99</td>
    <td align="right">28.86</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.04</td>
    <td align="right">30.09</td>
    <td align="right">29.84</td>
    <td align="right">33.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">167.18</td>
    <td align="right">140.70</td>
    <td align="right">140.20</td>
    <td align="right">140.41</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.65</td>
    <td align="right">26.82</td>
    <td align="right">27.26</td>
    <td align="right">30.55</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.04</td>
    <td align="right">31.69</td>
    <td align="right">31.86</td>
    <td align="right">36.19</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.45</td>
    <td align="right">45.35</td>
    <td align="right">33.47</td>
    <td align="right">40.60</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.38</td>
    <td align="right">43.41</td>
    <td align="right">34.28</td>
    <td align="right">38.82</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.60</td>
    <td align="right">28.40</td>
    <td align="right">27.93</td>
    <td align="right">27.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.60</td>
    <td align="right">59.57</td>
    <td align="right">35.25</td>
    <td align="right">46.34</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.22</td>
    <td align="right">59.93</td>
    <td align="right">36.90</td>
    <td align="right">48.40</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.89</td>
    <td align="right">37.48</td>
    <td align="right">27.50</td>
    <td align="right">37.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.76</td>
    <td align="right">77.32</td>
    <td align="right">35.82</td>
    <td align="right">57.01</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.82</td>
    <td align="right">78.40</td>
    <td align="right">37.89</td>
    <td align="right">58.41</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.06</td>
    <td align="right">53.90</td>
    <td align="right">36.83</td>
    <td align="right">49.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">47.30</td>
    <td align="right">89.09</td>
    <td align="right">34.56</td>
    <td align="right">61.97</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.55</td>
    <td align="right">96.19</td>
    <td align="right">38.60</td>
    <td align="right">67.75</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.11</td>
    <td align="right">54.22</td>
    <td align="right">37.45</td>
    <td align="right">50.15</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.40</td>
    <td align="right">42.15</td>
    <td align="right">42.34</td>
    <td align="right">42.20</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.56</td>
    <td align="right">42.82</td>
    <td align="right">42.64</td>
    <td align="right">42.40</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.61</td>
    <td align="right">28.08</td>
    <td align="right">27.99</td>
    <td align="right">27.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.59</td>
    <td align="right">55.69</td>
    <td align="right">55.16</td>
    <td align="right">55.87</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.06</td>
    <td align="right">56.03</td>
    <td align="right">55.39</td>
    <td align="right">56.53</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.86</td>
    <td align="right">37.15</td>
    <td align="right">37.14</td>
    <td align="right">37.15</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.75</td>
    <td align="right">75.38</td>
    <td align="right">76.80</td>
    <td align="right">75.68</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">41.81</td>
    <td align="right">76.23</td>
    <td align="right">74.72</td>
    <td align="right">75.92</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.11</td>
    <td align="right">47.19</td>
    <td align="right">47.15</td>
    <td align="right">47.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.14</td>
    <td align="right">84.17</td>
    <td align="right">84.63</td>
    <td align="right">84.06</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.59</td>
    <td align="right">89.67</td>
    <td align="right">88.50</td>
    <td align="right">90.52</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.08</td>
    <td align="right">47.76</td>
    <td align="right">47.43</td>
    <td align="right">47.43</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.93</td>
    <td align="right">28.21</td>
    <td align="right">28.14</td>
    <td align="right">27.72</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.79</td>
    <td align="right">30.63</td>
    <td align="right">30.24</td>
    <td align="right">30.10</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.34</td>
    <td align="right">30.57</td>
    <td align="right">30.34</td>
    <td align="right">30.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.06</td>
    <td align="right">44.16</td>
    <td align="right">34.31</td>
    <td align="right">44.11</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.86</td>
    <td align="right">38.76</td>
    <td align="right">28.97</td>
    <td align="right">38.69</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.76</td>
    <td align="right">46.69</td>
    <td align="right">36.94</td>
    <td align="right">46.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.09</td>
    <td align="right">53.29</td>
    <td align="right">36.42</td>
    <td align="right">49.72</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.90</td>
    <td align="right">57.56</td>
    <td align="right">39.74</td>
    <td align="right">52.90</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.68</td>
    <td align="right">57.19</td>
    <td align="right">39.34</td>
    <td align="right">53.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.11</td>
    <td align="right">53.79</td>
    <td align="right">36.77</td>
    <td align="right">49.80</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.67</td>
    <td align="right">59.45</td>
    <td align="right">40.12</td>
    <td align="right">54.53</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.98</td>
    <td align="right">58.98</td>
    <td align="right">39.82</td>
    <td align="right">53.64</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.94</td>
    <td align="right">27.76</td>
    <td align="right">27.75</td>
    <td align="right">27.79</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.84</td>
    <td align="right">30.24</td>
    <td align="right">30.16</td>
    <td align="right">30.16</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.37</td>
    <td align="right">30.56</td>
    <td align="right">30.31</td>
    <td align="right">30.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.00</td>
    <td align="right">37.93</td>
    <td align="right">37.52</td>
    <td align="right">37.70</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.91</td>
    <td align="right">38.09</td>
    <td align="right">37.82</td>
    <td align="right">37.93</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.75</td>
    <td align="right">38.61</td>
    <td align="right">38.57</td>
    <td align="right">38.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.13</td>
    <td align="right">47.40</td>
    <td align="right">47.07</td>
    <td align="right">47.10</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.85</td>
    <td align="right">49.84</td>
    <td align="right">49.57</td>
    <td align="right">49.57</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.71</td>
    <td align="right">49.61</td>
    <td align="right">49.62</td>
    <td align="right">49.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.08</td>
    <td align="right">47.62</td>
    <td align="right">47.43</td>
    <td align="right">47.38</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.62</td>
    <td align="right">52.36</td>
    <td align="right">52.19</td>
    <td align="right">52.15</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.00</td>
    <td align="right">52.16</td>
    <td align="right">51.89</td>
    <td align="right">51.91</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.02</td>
    <td align="right">44.09</td>
    <td align="right">33.04</td>
    <td align="right">39.22</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.78</td>
    <td align="right">55.23</td>
    <td align="right">36.91</td>
    <td align="right">46.57</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.38</td>
    <td align="right">62.86</td>
    <td align="right">38.67</td>
    <td align="right">50.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.67</td>
    <td align="right">61.23</td>
    <td align="right">34.55</td>
    <td align="right">48.13</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.94</td>
    <td align="right">61.56</td>
    <td align="right">35.14</td>
    <td align="right">49.26</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.73</td>
    <td align="right">81.58</td>
    <td align="right">40.17</td>
    <td align="right">60.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.90</td>
    <td align="right">74.10</td>
    <td align="right">33.74</td>
    <td align="right">54.74</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.28</td>
    <td align="right">79.99</td>
    <td align="right">36.39</td>
    <td align="right">59.16</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.27</td>
    <td align="right">93.05</td>
    <td align="right">38.37</td>
    <td align="right">64.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.39</td>
    <td align="right">100.32</td>
    <td align="right">34.63</td>
    <td align="right">68.28</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.63</td>
    <td align="right">99.98</td>
    <td align="right">36.31</td>
    <td align="right">69.51</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.62</td>
    <td align="right">120.57</td>
    <td align="right">39.90</td>
    <td align="right">80.08</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.01</td>
    <td align="right">43.29</td>
    <td align="right">42.77</td>
    <td align="right">43.01</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.80</td>
    <td align="right">47.55</td>
    <td align="right">47.79</td>
    <td align="right">47.59</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.40</td>
    <td align="right">62.11</td>
    <td align="right">62.19</td>
    <td align="right">62.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.85</td>
    <td align="right">57.08</td>
    <td align="right">57.26</td>
    <td align="right">56.96</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">40.17</td>
    <td align="right">60.68</td>
    <td align="right">60.35</td>
    <td align="right">60.25</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.74</td>
    <td align="right">78.06</td>
    <td align="right">78.55</td>
    <td align="right">78.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.92</td>
    <td align="right">66.93</td>
    <td align="right">67.02</td>
    <td align="right">66.90</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.40</td>
    <td align="right">77.17</td>
    <td align="right">76.96</td>
    <td align="right">76.92</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">47.04</td>
    <td align="right">86.90</td>
    <td align="right">83.57</td>
    <td align="right">83.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.68</td>
    <td align="right">90.91</td>
    <td align="right">91.08</td>
    <td align="right">91.58</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.67</td>
    <td align="right">92.40</td>
    <td align="right">92.02</td>
    <td align="right">92.01</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.05</td>
    <td align="right">117.91</td>
    <td align="right">117.85</td>
    <td align="right">117.91</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.33</td>
    <td align="right">33.65</td>
    <td align="right">15.52</td>
    <td align="right">37.28</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">72.92</td>
    <td align="right">62.38</td>
    <td align="right">42.46</td>
    <td align="right">52.08</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.23</td>
    <td align="right">20.74</td>
    <td align="right">23.40</td>
    <td align="right">25.62</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.76</td>
    <td align="right">26.90</td>
    <td align="right">28.17</td>
    <td align="right">30.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">116.99</td>
    <td align="right">99.40</td>
    <td align="right">45.54</td>
    <td align="right">73.15</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.24</td>
    <td align="right">24.90</td>
    <td align="right">26.90</td>
    <td align="right">29.68</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">32.90</td>
    <td align="right">32.27</td>
    <td align="right">32.61</td>
    <td align="right">34.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">254.43</td>
    <td align="right">215.04</td>
    <td align="right">63.83</td>
    <td align="right">139.95</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.24</td>
    <td align="right">37.49</td>
    <td align="right">38.17</td>
    <td align="right">41.64</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.31</td>
    <td align="right">49.21</td>
    <td align="right">48.44</td>
    <td align="right">52.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">437.49</td>
    <td align="right">355.31</td>
    <td align="right">79.39</td>
    <td align="right">219.21</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">44.91</td>
    <td align="right">44.37</td>
    <td align="right">45.26</td>
    <td align="right">49.75</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.71</td>
    <td align="right">61.44</td>
    <td align="right">62.37</td>
    <td align="right">65.82</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">70.55</td>
    <td align="right">64.97</td>
    <td align="right">65.50</td>
    <td align="right">64.76</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.31</td>
    <td align="right">20.73</td>
    <td align="right">23.23</td>
    <td align="right">25.70</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.72</td>
    <td align="right">27.20</td>
    <td align="right">28.45</td>
    <td align="right">29.40</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">116.94</td>
    <td align="right">104.54</td>
    <td align="right">104.13</td>
    <td align="right">105.52</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">45.45</td>
    <td align="right">44.76</td>
    <td align="right">46.90</td>
    <td align="right">51.19</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">32.11</td>
    <td align="right">32.41</td>
    <td align="right">32.89</td>
    <td align="right">35.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">256.63</td>
    <td align="right">221.31</td>
    <td align="right">221.65</td>
    <td align="right">221.30</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.30</td>
    <td align="right">37.52</td>
    <td align="right">38.04</td>
    <td align="right">42.27</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.31</td>
    <td align="right">47.97</td>
    <td align="right">46.82</td>
    <td align="right">50.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">435.35</td>
    <td align="right">360.86</td>
    <td align="right">361.00</td>
    <td align="right">361.29</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">44.96</td>
    <td align="right">44.54</td>
    <td align="right">45.41</td>
    <td align="right">49.74</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.59</td>
    <td align="right">61.92</td>
    <td align="right">62.42</td>
    <td align="right">66.07</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.10</td>
    <td align="right">43.69</td>
    <td align="right">34.74</td>
    <td align="right">40.44</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">29.02</td>
    <td align="right">45.00</td>
    <td align="right">36.85</td>
    <td align="right">40.83</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.10</td>
    <td align="right">30.34</td>
    <td align="right">30.30</td>
    <td align="right">30.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.20</td>
    <td align="right">61.71</td>
    <td align="right">38.60</td>
    <td align="right">50.27</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.34</td>
    <td align="right">62.66</td>
    <td align="right">41.78</td>
    <td align="right">52.37</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">20.14</td>
    <td align="right">42.07</td>
    <td align="right">31.87</td>
    <td align="right">42.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">56.83</td>
    <td align="right">90.43</td>
    <td align="right">50.53</td>
    <td align="right">71.08</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.11</td>
    <td align="right">95.02</td>
    <td align="right">58.49</td>
    <td align="right">77.31</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.93</td>
    <td align="right">78.18</td>
    <td align="right">60.92</td>
    <td align="right">74.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.42</td>
    <td align="right">112.64</td>
    <td align="right">60.89</td>
    <td align="right">87.25</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.74</td>
    <td align="right">126.48</td>
    <td align="right">74.12</td>
    <td align="right">101.10</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.71</td>
    <td align="right">90.16</td>
    <td align="right">74.51</td>
    <td align="right">86.74</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">26.12</td>
    <td align="right">43.98</td>
    <td align="right">44.18</td>
    <td align="right">44.11</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.64</td>
    <td align="right">42.99</td>
    <td align="right">42.87</td>
    <td align="right">42.67</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.25</td>
    <td align="right">30.41</td>
    <td align="right">30.44</td>
    <td align="right">30.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.82</td>
    <td align="right">57.69</td>
    <td align="right">57.09</td>
    <td align="right">57.64</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.98</td>
    <td align="right">59.46</td>
    <td align="right">58.53</td>
    <td align="right">60.37</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">20.08</td>
    <td align="right">42.10</td>
    <td align="right">41.61</td>
    <td align="right">41.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.28</td>
    <td align="right">88.61</td>
    <td align="right">89.82</td>
    <td align="right">88.70</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">63.67</td>
    <td align="right">92.63</td>
    <td align="right">91.04</td>
    <td align="right">92.21</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">61.74</td>
    <td align="right">86.48</td>
    <td align="right">86.77</td>
    <td align="right">86.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.53</td>
    <td align="right">107.30</td>
    <td align="right">107.52</td>
    <td align="right">107.35</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">85.42</td>
    <td align="right">118.82</td>
    <td align="right">117.89</td>
    <td align="right">120.15</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.74</td>
    <td align="right">85.25</td>
    <td align="right">84.95</td>
    <td align="right">85.59</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.28</td>
    <td align="right">29.90</td>
    <td align="right">29.86</td>
    <td align="right">29.85</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.11</td>
    <td align="right">32.03</td>
    <td align="right">31.97</td>
    <td align="right">31.99</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.60</td>
    <td align="right">31.93</td>
    <td align="right">31.82</td>
    <td align="right">31.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">20.53</td>
    <td align="right">48.72</td>
    <td align="right">38.84</td>
    <td align="right">48.88</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.46</td>
    <td align="right">41.97</td>
    <td align="right">32.15</td>
    <td align="right">42.01</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.48</td>
    <td align="right">52.13</td>
    <td align="right">43.04</td>
    <td align="right">53.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.78</td>
    <td align="right">77.70</td>
    <td align="right">62.21</td>
    <td align="right">74.87</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.03</td>
    <td align="right">81.06</td>
    <td align="right">63.29</td>
    <td align="right">76.49</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">52.95</td>
    <td align="right">80.95</td>
    <td align="right">62.98</td>
    <td align="right">77.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.63</td>
    <td align="right">92.64</td>
    <td align="right">75.74</td>
    <td align="right">88.66</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.74</td>
    <td align="right">97.58</td>
    <td align="right">77.59</td>
    <td align="right">92.54</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.01</td>
    <td align="right">98.14</td>
    <td align="right">77.99</td>
    <td align="right">92.66</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.26</td>
    <td align="right">29.89</td>
    <td align="right">29.86</td>
    <td align="right">29.86</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.11</td>
    <td align="right">32.46</td>
    <td align="right">32.45</td>
    <td align="right">32.49</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.64</td>
    <td align="right">31.91</td>
    <td align="right">31.83</td>
    <td align="right">31.83</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">22.19</td>
    <td align="right">43.15</td>
    <td align="right">42.62</td>
    <td align="right">42.97</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">21.93</td>
    <td align="right">42.34</td>
    <td align="right">42.19</td>
    <td align="right">42.25</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">24.69</td>
    <td align="right">44.17</td>
    <td align="right">44.87</td>
    <td align="right">44.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.31</td>
    <td align="right">71.21</td>
    <td align="right">71.88</td>
    <td align="right">71.83</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">55.69</td>
    <td align="right">76.25</td>
    <td align="right">76.68</td>
    <td align="right">76.43</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">54.58</td>
    <td align="right">74.48</td>
    <td align="right">74.62</td>
    <td align="right">74.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.84</td>
    <td align="right">85.77</td>
    <td align="right">86.07</td>
    <td align="right">86.08</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.48</td>
    <td align="right">89.65</td>
    <td align="right">89.87</td>
    <td align="right">89.81</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.86</td>
    <td align="right">91.11</td>
    <td align="right">89.90</td>
    <td align="right">90.03</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.88</td>
    <td align="right">43.70</td>
    <td align="right">35.29</td>
    <td align="right">40.21</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.69</td>
    <td align="right">55.36</td>
    <td align="right">39.14</td>
    <td align="right">47.43</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">43.55</td>
    <td align="right">63.39</td>
    <td align="right">40.83</td>
    <td align="right">51.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.13</td>
    <td align="right">64.51</td>
    <td align="right">38.14</td>
    <td align="right">51.40</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">50.55</td>
    <td align="right">67.68</td>
    <td align="right">44.58</td>
    <td align="right">58.30</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">49.65</td>
    <td align="right">83.41</td>
    <td align="right">42.29</td>
    <td align="right">62.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.40</td>
    <td align="right">86.99</td>
    <td align="right">50.27</td>
    <td align="right">69.36</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">83.02</td>
    <td align="right">108.58</td>
    <td align="right">72.36</td>
    <td align="right">91.87</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">77.77</td>
    <td align="right">111.95</td>
    <td align="right">51.92</td>
    <td align="right">80.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">78.86</td>
    <td align="right">120.80</td>
    <td align="right">61.95</td>
    <td align="right">92.19</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.47</td>
    <td align="right">129.54</td>
    <td align="right">73.01</td>
    <td align="right">104.38</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.41</td>
    <td align="right">148.41</td>
    <td align="right">62.48</td>
    <td align="right">106.33</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.99</td>
    <td align="right">43.48</td>
    <td align="right">42.78</td>
    <td align="right">42.88</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.82</td>
    <td align="right">48.47</td>
    <td align="right">48.69</td>
    <td align="right">48.53</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">42.99</td>
    <td align="right">64.08</td>
    <td align="right">64.11</td>
    <td align="right">64.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.22</td>
    <td align="right">59.02</td>
    <td align="right">59.04</td>
    <td align="right">58.88</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">47.42</td>
    <td align="right">68.70</td>
    <td align="right">68.29</td>
    <td align="right">68.06</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">50.88</td>
    <td align="right">81.14</td>
    <td align="right">81.53</td>
    <td align="right">81.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">57.60</td>
    <td align="right">75.48</td>
    <td align="right">75.51</td>
    <td align="right">75.43</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">71.55</td>
    <td align="right">101.34</td>
    <td align="right">101.60</td>
    <td align="right">101.22</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">79.94</td>
    <td align="right">107.55</td>
    <td align="right">105.23</td>
    <td align="right">105.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">79.02</td>
    <td align="right">109.42</td>
    <td align="right">109.54</td>
    <td align="right">109.77</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.52</td>
    <td align="right">127.26</td>
    <td align="right">127.02</td>
    <td align="right">127.10</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">109.72</td>
    <td align="right">145.48</td>
    <td align="right">145.40</td>
    <td align="right">145.58</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
