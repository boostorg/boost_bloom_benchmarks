# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.35</td>
    <td align="right">6.17</td>
    <td align="right">4.55</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.79</td>
    <td align="right">11.69</td>
    <td align="right">17.99</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.86</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.90</td>
    <td align="right">4.95</td>
    <td align="right">4.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.81</td>
    <td align="right">17.38</td>
    <td align="right">18.81</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.41</td>
    <td align="right">5.04</td>
    <td align="right">5.05</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.48</td>
    <td align="right">5.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">22.49</td>
    <td align="right">19.97</td>
    <td align="right">17.70</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.99</td>
    <td align="right">5.30</td>
    <td align="right">5.30</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.83</td>
    <td align="right">5.94</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.01</td>
    <td align="right">24.91</td>
    <td align="right">18.10</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.60</td>
    <td align="right">5.77</td>
    <td align="right">5.76</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.14</td>
    <td align="right">12.30</td>
    <td align="right">18.36</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.78</td>
    <td align="right">4.60</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.54</td>
    <td align="right">5.14</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.98</td>
    <td align="right">18.15</td>
    <td align="right">19.36</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.28</td>
    <td align="right">5.15</td>
    <td align="right">5.15</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.16</td>
    <td align="right">5.74</td>
    <td align="right">5.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.64</td>
    <td align="right">21.62</td>
    <td align="right">18.47</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.79</td>
    <td align="right">5.69</td>
    <td align="right">5.69</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.39</td>
    <td align="right">6.13</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.61</td>
    <td align="right">27.72</td>
    <td align="right">18.64</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.13</td>
    <td align="right">6.08</td>
    <td align="right">6.07</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.93</td>
    <td align="right">6.45</td>
    <td align="right">6.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.19</td>
    <td align="right">5.56</td>
    <td align="right">5.56</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.87</td>
    <td align="right">7.06</td>
    <td align="right">7.05</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.24</td>
    <td align="right">3.41</td>
    <td align="right">3.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.12</td>
    <td align="right">7.75</td>
    <td align="right">7.75</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.23</td>
    <td align="right">9.55</td>
    <td align="right">9.55</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.56</td>
    <td align="right">3.09</td>
    <td align="right">3.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.23</td>
    <td align="right">11.33</td>
    <td align="right">11.32</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">22.37</td>
    <td align="right">13.57</td>
    <td align="right">13.57</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">6.18</td>
    <td align="right">5.91</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.39</td>
    <td align="right">13.03</td>
    <td align="right">12.98</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.21</td>
    <td align="right">15.95</td>
    <td align="right">15.96</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">6.20</td>
    <td align="right">5.94</td>
    <td align="right">4.17</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.04</td>
    <td align="right">5.68</td>
    <td align="right">5.68</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.92</td>
    <td align="right">6.94</td>
    <td align="right">6.94</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.25</td>
    <td align="right">2.97</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">6.34</td>
    <td align="right">7.90</td>
    <td align="right">7.90</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.88</td>
    <td align="right">9.42</td>
    <td align="right">9.41</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.69</td>
    <td align="right">2.75</td>
    <td align="right">2.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.84</td>
    <td align="right">11.20</td>
    <td align="right">11.34</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">21.61</td>
    <td align="right">13.76</td>
    <td align="right">13.75</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">6.14</td>
    <td align="right">6.12</td>
    <td align="right">4.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.65</td>
    <td align="right">13.01</td>
    <td align="right">13.00</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.55</td>
    <td align="right">15.87</td>
    <td align="right">15.94</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">6.19</td>
    <td align="right">6.15</td>
    <td align="right">4.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.22</td>
    <td align="right">3.23</td>
    <td align="right">3.23</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.60</td>
    <td align="right">5.24</td>
    <td align="right">5.22</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.73</td>
    <td align="right">5.10</td>
    <td align="right">5.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.36</td>
    <td align="right">3.36</td>
    <td align="right">3.32</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.41</td>
    <td align="right">4.47</td>
    <td align="right">4.46</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.76</td>
    <td align="right">5.22</td>
    <td align="right">5.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.61</td>
    <td align="right">5.56</td>
    <td align="right">3.95</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.63</td>
    <td align="right">8.20</td>
    <td align="right">6.21</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.94</td>
    <td align="right">7.92</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.67</td>
    <td align="right">5.61</td>
    <td align="right">3.95</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.18</td>
    <td align="right">9.50</td>
    <td align="right">6.25</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">9.03</td>
    <td align="right">9.17</td>
    <td align="right">6.19</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.23</td>
    <td align="right">2.81</td>
    <td align="right">2.78</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.61</td>
    <td align="right">4.87</td>
    <td align="right">4.86</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.73</td>
    <td align="right">4.67</td>
    <td align="right">4.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.37</td>
    <td align="right">2.88</td>
    <td align="right">2.87</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.77</td>
    <td align="right">4.79</td>
    <td align="right">4.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.43</td>
    <td align="right">5.71</td>
    <td align="right">3.91</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.21</td>
    <td align="right">8.34</td>
    <td align="right">6.25</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">8.66</td>
    <td align="right">7.98</td>
    <td align="right">6.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.48</td>
    <td align="right">5.76</td>
    <td align="right">3.95</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.89</td>
    <td align="right">9.73</td>
    <td align="right">6.40</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">9.33</td>
    <td align="right">9.19</td>
    <td align="right">6.24</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">48.03</td>
    <td align="right">24.25</td>
    <td align="right">15.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">17.04</td>
    <td align="right">14.62</td>
    <td align="right">20.50</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.44</td>
    <td align="right">6.23</td>
    <td align="right">6.24</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">6.29</td>
    <td align="right">6.14</td>
    <td align="right">6.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">50.20</td>
    <td align="right">49.65</td>
    <td align="right">25.95</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.52</td>
    <td align="right">11.14</td>
    <td align="right">11.12</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">12.15</td>
    <td align="right">12.46</td>
    <td align="right">13.08</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">85.96</td>
    <td align="right">81.23</td>
    <td align="right">30.67</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.41</td>
    <td align="right">17.92</td>
    <td align="right">17.91</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">18.98</td>
    <td align="right">18.92</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">125.45</td>
    <td align="right">117.22</td>
    <td align="right">37.06</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">21.82</td>
    <td align="right">21.80</td>
    <td align="right">21.80</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">25.41</td>
    <td align="right">22.57</td>
    <td align="right">22.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.03</td>
    <td align="right">15.70</td>
    <td align="right">20.97</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.64</td>
    <td align="right">5.48</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.08</td>
    <td align="right">6.14</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">54.31</td>
    <td align="right">59.42</td>
    <td align="right">29.47</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.40</td>
    <td align="right">11.55</td>
    <td align="right">11.59</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.46</td>
    <td align="right">12.74</td>
    <td align="right">12.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.73</td>
    <td align="right">91.46</td>
    <td align="right">33.62</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.39</td>
    <td align="right">18.41</td>
    <td align="right">18.34</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.90</td>
    <td align="right">19.07</td>
    <td align="right">19.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.29</td>
    <td align="right">133.83</td>
    <td align="right">40.02</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.39</td>
    <td align="right">21.95</td>
    <td align="right">21.95</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">23.14</td>
    <td align="right">23.14</td>
    <td align="right">23.32</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.78</td>
    <td align="right">7.21</td>
    <td align="right">7.20</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">7.04</td>
    <td align="right">8.41</td>
    <td align="right">8.41</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.78</td>
    <td align="right">5.13</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.09</td>
    <td align="right">15.43</td>
    <td align="right">15.38</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">17.10</td>
    <td align="right">18.94</td>
    <td align="right">18.88</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.53</td>
    <td align="right">8.70</td>
    <td align="right">8.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">30.58</td>
    <td align="right">30.30</td>
    <td align="right">30.24</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">38.00</td>
    <td align="right">33.31</td>
    <td align="right">33.30</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">19.36</td>
    <td align="right">20.33</td>
    <td align="right">14.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">39.51</td>
    <td align="right">39.23</td>
    <td align="right">39.18</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">41.25</td>
    <td align="right">51.33</td>
    <td align="right">51.32</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">22.30</td>
    <td align="right">23.35</td>
    <td align="right">16.64</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.97</td>
    <td align="right">7.75</td>
    <td align="right">7.72</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.22</td>
    <td align="right">9.37</td>
    <td align="right">9.39</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.52</td>
    <td align="right">4.33</td>
    <td align="right">4.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.09</td>
    <td align="right">14.46</td>
    <td align="right">14.56</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.70</td>
    <td align="right">17.81</td>
    <td align="right">17.74</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.71</td>
    <td align="right">8.01</td>
    <td align="right">8.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">30.26</td>
    <td align="right">30.87</td>
    <td align="right">30.89</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">37.70</td>
    <td align="right">34.05</td>
    <td align="right">34.06</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">20.53</td>
    <td align="right">20.92</td>
    <td align="right">15.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.69</td>
    <td align="right">39.36</td>
    <td align="right">39.30</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">41.57</td>
    <td align="right">51.52</td>
    <td align="right">51.55</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">24.13</td>
    <td align="right">24.18</td>
    <td align="right">17.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.99</td>
    <td align="right">4.14</td>
    <td align="right">4.12</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">6.34</td>
    <td align="right">7.37</td>
    <td align="right">7.14</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">6.28</td>
    <td align="right">6.94</td>
    <td align="right">6.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">8.43</td>
    <td align="right">9.30</td>
    <td align="right">9.25</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">9.35</td>
    <td align="right">11.15</td>
    <td align="right">11.14</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">10.47</td>
    <td align="right">12.52</td>
    <td align="right">12.34</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">18.25</td>
    <td align="right">19.12</td>
    <td align="right">14.82</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.00</td>
    <td align="right">26.37</td>
    <td align="right">21.68</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">25.97</td>
    <td align="right">26.31</td>
    <td align="right">21.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">20.94</td>
    <td align="right">21.40</td>
    <td align="right">16.32</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">32.54</td>
    <td align="right">36.07</td>
    <td align="right">24.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.70</td>
    <td align="right">33.18</td>
    <td align="right">24.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.41</td>
    <td align="right">4.05</td>
    <td align="right">4.03</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.36</td>
    <td align="right">5.54</td>
    <td align="right">5.54</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
    <td align="right">5.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.66</td>
    <td align="right">8.44</td>
    <td align="right">8.41</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.86</td>
    <td align="right">9.82</td>
    <td align="right">9.85</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.74</td>
    <td align="right">12.25</td>
    <td align="right">12.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">17.53</td>
    <td align="right">20.97</td>
    <td align="right">14.98</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.71</td>
    <td align="right">26.52</td>
    <td align="right">21.99</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">25.79</td>
    <td align="right">26.15</td>
    <td align="right">21.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">19.96</td>
    <td align="right">23.73</td>
    <td align="right">16.56</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.51</td>
    <td align="right">36.99</td>
    <td align="right">25.30</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">32.66</td>
    <td align="right">36.62</td>
    <td align="right">25.01</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.55</td>
    <td align="right">5.83</td>
    <td align="right">4.28</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.49</td>
    <td align="right">10.50</td>
    <td align="right">17.07</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.58</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.11</td>
    <td align="right">4.66</td>
    <td align="right">4.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">14.73</td>
    <td align="right">15.41</td>
    <td align="right">18.48</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.15</td>
    <td align="right">4.65</td>
    <td align="right">4.65</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.67</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.82</td>
    <td align="right">18.57</td>
    <td align="right">17.09</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.64</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.00</td>
    <td align="right">5.95</td>
    <td align="right">5.95</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.87</td>
    <td align="right">23.20</td>
    <td align="right">17.97</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.00</td>
    <td align="right">5.61</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">3.30</td>
    <td align="right">3.48</td>
    <td align="right">3.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.63</td>
    <td align="right">11.21</td>
    <td align="right">17.65</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.83</td>
    <td align="right">4.30</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.22</td>
    <td align="right">4.87</td>
    <td align="right">4.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.34</td>
    <td align="right">16.28</td>
    <td align="right">19.07</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">5.24</td>
    <td align="right">4.74</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.81</td>
    <td align="right">5.60</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">19.16</td>
    <td align="right">19.98</td>
    <td align="right">17.60</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.83</td>
    <td align="right">5.17</td>
    <td align="right">5.17</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.14</td>
    <td align="right">6.04</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.03</td>
    <td align="right">24.48</td>
    <td align="right">18.01</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">6.11</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.46</td>
    <td align="right">3.71</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.31</td>
    <td align="right">3.89</td>
    <td align="right">3.88</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.42</td>
    <td align="right">3.74</td>
    <td align="right">3.77</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.79</td>
    <td align="right">2.53</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.02</td>
    <td align="right">3.90</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.00</td>
    <td align="right">4.04</td>
    <td align="right">4.04</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.26</td>
    <td align="right">2.31</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.81</td>
    <td align="right">6.45</td>
    <td align="right">6.46</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">6.12</td>
    <td align="right">6.35</td>
    <td align="right">6.53</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.37</td>
    <td align="right">4.33</td>
    <td align="right">3.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.51</td>
    <td align="right">7.45</td>
    <td align="right">7.26</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.98</td>
    <td align="right">7.67</td>
    <td align="right">7.67</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.42</td>
    <td align="right">4.36</td>
    <td align="right">3.25</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.46</td>
    <td align="right">4.15</td>
    <td align="right">4.14</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.54</td>
    <td align="right">4.00</td>
    <td align="right">3.99</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.05</td>
    <td align="right">2.81</td>
    <td align="right">2.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.92</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.17</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">3.26</td>
    <td align="right">2.55</td>
    <td align="right">2.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">6.29</td>
    <td align="right">7.08</td>
    <td align="right">6.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.50</td>
    <td align="right">6.76</td>
    <td align="right">6.79</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.67</td>
    <td align="right">4.69</td>
    <td align="right">3.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.57</td>
    <td align="right">7.49</td>
    <td align="right">7.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.13</td>
    <td align="right">7.82</td>
    <td align="right">7.63</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.70</td>
    <td align="right">4.72</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.80</td>
    <td align="right">2.36</td>
    <td align="right">2.36</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.89</td>
    <td align="right">4.11</td>
    <td align="right">4.10</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.95</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.89</td>
    <td align="right">2.40</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.21</td>
    <td align="right">3.82</td>
    <td align="right">3.83</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.12</td>
    <td align="right">4.01</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.49</td>
    <td align="right">4.29</td>
    <td align="right">2.99</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.85</td>
    <td align="right">6.32</td>
    <td align="right">4.70</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">6.03</td>
    <td align="right">6.07</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.54</td>
    <td align="right">4.30</td>
    <td align="right">3.01</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.94</td>
    <td align="right">7.13</td>
    <td align="right">4.64</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">7.26</td>
    <td align="right">6.84</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.99</td>
    <td align="right">2.63</td>
    <td align="right">2.66</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.05</td>
    <td align="right">4.44</td>
    <td align="right">4.43</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.14</td>
    <td align="right">4.17</td>
    <td align="right">4.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.14</td>
    <td align="right">2.71</td>
    <td align="right">2.71</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.96</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.34</td>
    <td align="right">4.25</td>
    <td align="right">4.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.74</td>
    <td align="right">4.54</td>
    <td align="right">3.31</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">6.24</td>
    <td align="right">6.42</td>
    <td align="right">5.25</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.36</td>
    <td align="right">6.40</td>
    <td align="right">4.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.79</td>
    <td align="right">4.57</td>
    <td align="right">3.26</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.24</td>
    <td align="right">7.47</td>
    <td align="right">5.29</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.56</td>
    <td align="right">7.31</td>
    <td align="right">5.20</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">50.64</td>
    <td align="right">23.68</td>
    <td align="right">14.48</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">13.20</td>
    <td align="right">14.19</td>
    <td align="right">19.72</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.39</td>
    <td align="right">6.00</td>
    <td align="right">6.00</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.26</td>
    <td align="right">5.96</td>
    <td align="right">6.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">42.66</td>
    <td align="right">41.82</td>
    <td align="right">25.23</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.89</td>
    <td align="right">10.69</td>
    <td align="right">10.65</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">11.86</td>
    <td align="right">13.17</td>
    <td align="right">13.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">71.84</td>
    <td align="right">74.62</td>
    <td align="right">30.25</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">16.29</td>
    <td align="right">17.63</td>
    <td align="right">18.82</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.76</td>
    <td align="right">20.36</td>
    <td align="right">20.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">103.12</td>
    <td align="right">103.30</td>
    <td align="right">35.17</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">19.36</td>
    <td align="right">21.50</td>
    <td align="right">21.49</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.54</td>
    <td align="right">15.26</td>
    <td align="right">15.26</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">12.21</td>
    <td align="right">12.85</td>
    <td align="right">19.53</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.78</td>
    <td align="right">5.25</td>
    <td align="right">5.27</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.12</td>
    <td align="right">5.95</td>
    <td align="right">5.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">44.76</td>
    <td align="right">45.94</td>
    <td align="right">25.97</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.78</td>
    <td align="right">10.00</td>
    <td align="right">9.97</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.26</td>
    <td align="right">12.56</td>
    <td align="right">12.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.01</td>
    <td align="right">84.72</td>
    <td align="right">31.07</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.59</td>
    <td align="right">17.73</td>
    <td align="right">17.73</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.86</td>
    <td align="right">20.58</td>
    <td align="right">20.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">122.32</td>
    <td align="right">119.19</td>
    <td align="right">36.43</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.36</td>
    <td align="right">21.67</td>
    <td align="right">21.68</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.70</td>
    <td align="right">16.59</td>
    <td align="right">16.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.55</td>
    <td align="right">5.25</td>
    <td align="right">5.30</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.06</td>
    <td align="right">4.40</td>
    <td align="right">4.41</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.43</td>
    <td align="right">3.25</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.91</td>
    <td align="right">9.17</td>
    <td align="right">9.16</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.69</td>
    <td align="right">11.11</td>
    <td align="right">11.15</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.95</td>
    <td align="right">7.26</td>
    <td align="right">7.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">19.37</td>
    <td align="right">21.05</td>
    <td align="right">21.09</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.84</td>
    <td align="right">21.50</td>
    <td align="right">21.51</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.70</td>
    <td align="right">15.95</td>
    <td align="right">11.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">24.20</td>
    <td align="right">26.75</td>
    <td align="right">26.77</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">24.82</td>
    <td align="right">30.39</td>
    <td align="right">30.38</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">17.03</td>
    <td align="right">18.18</td>
    <td align="right">13.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.37</td>
    <td align="right">5.16</td>
    <td align="right">5.20</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.56</td>
    <td align="right">5.18</td>
    <td align="right">5.15</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">5.19</td>
    <td align="right">5.15</td>
    <td align="right">5.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">9.19</td>
    <td align="right">9.35</td>
    <td align="right">9.35</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.69</td>
    <td align="right">11.03</td>
    <td align="right">10.96</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">8.52</td>
    <td align="right">7.39</td>
    <td align="right">7.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.70</td>
    <td align="right">21.60</td>
    <td align="right">21.59</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.98</td>
    <td align="right">21.60</td>
    <td align="right">21.63</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.78</td>
    <td align="right">17.74</td>
    <td align="right">13.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.86</td>
    <td align="right">26.79</td>
    <td align="right">26.77</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">26.56</td>
    <td align="right">30.54</td>
    <td align="right">30.53</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.91</td>
    <td align="right">19.88</td>
    <td align="right">14.60</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.57</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.64</td>
    <td align="right">4.97</td>
    <td align="right">4.96</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.04</td>
    <td align="right">5.20</td>
    <td align="right">5.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">7.16</td>
    <td align="right">7.23</td>
    <td align="right">7.21</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">8.87</td>
    <td align="right">10.25</td>
    <td align="right">10.25</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">9.42</td>
    <td align="right">10.77</td>
    <td align="right">10.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.77</td>
    <td align="right">15.97</td>
    <td align="right">11.59</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.76</td>
    <td align="right">21.51</td>
    <td align="right">17.01</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">19.30</td>
    <td align="right">20.86</td>
    <td align="right">16.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">17.12</td>
    <td align="right">18.14</td>
    <td align="right">13.09</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">24.88</td>
    <td align="right">26.93</td>
    <td align="right">19.30</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">25.20</td>
    <td align="right">26.82</td>
    <td align="right">19.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.71</td>
    <td align="right">3.44</td>
    <td align="right">3.45</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.49</td>
    <td align="right">6.04</td>
    <td align="right">6.07</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.07</td>
    <td align="right">5.29</td>
    <td align="right">5.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.30</td>
    <td align="right">8.25</td>
    <td align="right">8.30</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.78</td>
    <td align="right">9.83</td>
    <td align="right">9.82</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.18</td>
    <td align="right">11.59</td>
    <td align="right">11.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">15.43</td>
    <td align="right">17.38</td>
    <td align="right">12.66</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">20.07</td>
    <td align="right">21.56</td>
    <td align="right">18.00</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.49</td>
    <td align="right">21.81</td>
    <td align="right">17.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.95</td>
    <td align="right">19.98</td>
    <td align="right">14.42</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">27.99</td>
    <td align="right">29.99</td>
    <td align="right">21.64</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.21</td>
    <td align="right">29.96</td>
    <td align="right">19.85</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.73</td>
    <td align="right">2.52</td>
    <td align="right">1.97</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">6.35</td>
    <td align="right">4.44</td>
    <td align="right">11.37</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.32</td>
    <td align="right">1.18</td>
    <td align="right">1.18</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">9.44</td>
    <td align="right">6.59</td>
    <td align="right">11.73</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.36</td>
    <td align="right">1.33</td>
    <td align="right">1.33</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.68</td>
    <td align="right">1.41</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">12.32</td>
    <td align="right">8.15</td>
    <td align="right">11.03</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.53</td>
    <td align="right">1.54</td>
    <td align="right">1.55</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.74</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">15.53</td>
    <td align="right">10.70</td>
    <td align="right">11.25</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">1.74</td>
    <td align="right">1.76</td>
    <td align="right">1.76</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.79</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.32</td>
    <td align="right">4.13</td>
    <td align="right">11.37</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">1.22</td>
    <td align="right">1.22</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">1.28</td>
    <td align="right">1.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.45</td>
    <td align="right">6.10</td>
    <td align="right">12.01</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.41</td>
    <td align="right">1.42</td>
    <td align="right">1.42</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.60</td>
    <td align="right">7.32</td>
    <td align="right">11.22</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.75</td>
    <td align="right">1.59</td>
    <td align="right">1.59</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">14.89</td>
    <td align="right">9.34</td>
    <td align="right">11.39</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.80</td>
    <td align="right">1.81</td>
    <td align="right">1.81</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.58</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.26</td>
    <td align="right">1.72</td>
    <td align="right">1.72</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.33</td>
    <td align="right">1.77</td>
    <td align="right">1.75</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.00</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.16</td>
    <td align="right">1.93</td>
    <td align="right">1.93</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.82</td>
    <td align="right">2.19</td>
    <td align="right">2.24</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.50</td>
    <td align="right">1.35</td>
    <td align="right">1.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.09</td>
    <td align="right">2.89</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.10</td>
    <td align="right">2.93</td>
    <td align="right">2.93</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">2.97</td>
    <td align="right">2.39</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.59</td>
    <td align="right">3.71</td>
    <td align="right">3.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.70</td>
    <td align="right">4.33</td>
    <td align="right">4.33</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">2.94</td>
    <td align="right">2.92</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.28</td>
    <td align="right">1.73</td>
    <td align="right">1.73</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.25</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">1.69</td>
    <td align="right">1.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.92</td>
    <td align="right">1.92</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">2.27</td>
    <td align="right">2.29</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.40</td>
    <td align="right">1.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.08</td>
    <td align="right">2.90</td>
    <td align="right">2.89</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.05</td>
    <td align="right">2.95</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.99</td>
    <td align="right">2.40</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.50</td>
    <td align="right">3.64</td>
    <td align="right">3.67</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.64</td>
    <td align="right">4.29</td>
    <td align="right">4.29</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.96</td>
    <td align="right">2.92</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.02</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.22</td>
    <td align="right">1.68</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.31</td>
    <td align="right">1.74</td>
    <td align="right">1.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.06</td>
    <td align="right">1.57</td>
    <td align="right">1.57</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.15</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">2.77</td>
    <td align="right">2.18</td>
    <td align="right">2.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">2.88</td>
    <td align="right">2.38</td>
    <td align="right">1.74</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.07</td>
    <td align="right">2.90</td>
    <td align="right">2.90</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.04</td>
    <td align="right">2.97</td>
    <td align="right">2.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">2.87</td>
    <td align="right">2.85</td>
    <td align="right">1.73</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.63</td>
    <td align="right">3.72</td>
    <td align="right">3.75</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.73</td>
    <td align="right">4.36</td>
    <td align="right">4.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.01</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.24</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.28</td>
    <td align="right">1.77</td>
    <td align="right">1.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.07</td>
    <td align="right">1.59</td>
    <td align="right">1.60</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.23</td>
    <td align="right">1.95</td>
    <td align="right">1.95</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.84</td>
    <td align="right">2.21</td>
    <td align="right">2.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.98</td>
    <td align="right">2.41</td>
    <td align="right">1.76</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.15</td>
    <td align="right">2.97</td>
    <td align="right">2.94</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.12</td>
    <td align="right">2.97</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.96</td>
    <td align="right">2.88</td>
    <td align="right">1.74</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.58</td>
    <td align="right">3.70</td>
    <td align="right">3.70</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.71</td>
    <td align="right">4.38</td>
    <td align="right">4.38</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.69</td>
    <td align="right">10.93</td>
    <td align="right">6.02</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">7.69</td>
    <td align="right">6.15</td>
    <td align="right">12.79</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">1.96</td>
    <td align="right">1.87</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">2.10</td>
    <td align="right">1.99</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">12.55</td>
    <td align="right">10.99</td>
    <td align="right">15.75</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">3.78</td>
    <td align="right">3.22</td>
    <td align="right">3.29</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">3.21</td>
    <td align="right">3.06</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">31.69</td>
    <td align="right">25.66</td>
    <td align="right">17.79</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">7.00</td>
    <td align="right">6.61</td>
    <td align="right">6.16</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.01</td>
    <td align="right">6.47</td>
    <td align="right">6.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">55.35</td>
    <td align="right">39.34</td>
    <td align="right">20.72</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.81</td>
    <td align="right">7.65</td>
    <td align="right">7.53</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.67</td>
    <td align="right">6.38</td>
    <td align="right">6.38</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.75</td>
    <td align="right">6.12</td>
    <td align="right">12.87</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.02</td>
    <td align="right">1.97</td>
    <td align="right">1.97</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.09</td>
    <td align="right">2.01</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">12.87</td>
    <td align="right">11.24</td>
    <td align="right">16.10</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.37</td>
    <td align="right">3.36</td>
    <td align="right">3.38</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.29</td>
    <td align="right">3.04</td>
    <td align="right">3.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">28.49</td>
    <td align="right">23.42</td>
    <td align="right">17.81</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.93</td>
    <td align="right">6.49</td>
    <td align="right">6.32</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.93</td>
    <td align="right">6.56</td>
    <td align="right">6.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">52.27</td>
    <td align="right">40.48</td>
    <td align="right">20.64</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.08</td>
    <td align="right">8.03</td>
    <td align="right">7.93</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.49</td>
    <td align="right">6.75</td>
    <td align="right">6.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.71</td>
    <td align="right">2.51</td>
    <td align="right">2.55</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.71</td>
    <td align="right">2.60</td>
    <td align="right">2.60</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.38</td>
    <td align="right">2.48</td>
    <td align="right">2.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">4.09</td>
    <td align="right">4.15</td>
    <td align="right">4.43</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.42</td>
    <td align="right">4.91</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.81</td>
    <td align="right">3.49</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.99</td>
    <td align="right">9.68</td>
    <td align="right">9.62</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.91</td>
    <td align="right">9.89</td>
    <td align="right">8.99</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">8.44</td>
    <td align="right">8.22</td>
    <td align="right">5.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">14.31</td>
    <td align="right">13.33</td>
    <td align="right">14.05</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.45</td>
    <td align="right">16.67</td>
    <td align="right">16.53</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.99</td>
    <td align="right">11.06</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.71</td>
    <td align="right">2.52</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.75</td>
    <td align="right">2.59</td>
    <td align="right">2.58</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.39</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.93</td>
    <td align="right">4.29</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.23</td>
    <td align="right">4.74</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">3.07</td>
    <td align="right">3.53</td>
    <td align="right">3.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.11</td>
    <td align="right">8.86</td>
    <td align="right">9.53</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">10.85</td>
    <td align="right">9.56</td>
    <td align="right">9.52</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.59</td>
    <td align="right">8.19</td>
    <td align="right">5.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">15.67</td>
    <td align="right">14.47</td>
    <td align="right">14.29</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">16.19</td>
    <td align="right">16.63</td>
    <td align="right">16.32</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.93</td>
    <td align="right">10.93</td>
    <td align="right">6.95</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.38</td>
    <td align="right">2.53</td>
    <td align="right">2.52</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">2.70</td>
    <td align="right">2.54</td>
    <td align="right">2.52</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">2.72</td>
    <td align="right">2.58</td>
    <td align="right">2.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.01</td>
    <td align="right">3.19</td>
    <td align="right">3.14</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.90</td>
    <td align="right">4.22</td>
    <td align="right">4.33</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.23</td>
    <td align="right">4.89</td>
    <td align="right">4.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">8.47</td>
    <td align="right">8.42</td>
    <td align="right">5.49</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.62</td>
    <td align="right">9.62</td>
    <td align="right">9.90</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.50</td>
    <td align="right">10.43</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.74</td>
    <td align="right">10.85</td>
    <td align="right">6.65</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.32</td>
    <td align="right">14.29</td>
    <td align="right">15.06</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">16.61</td>
    <td align="right">16.93</td>
    <td align="right">17.13</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.38</td>
    <td align="right">2.48</td>
    <td align="right">2.48</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.68</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.69</td>
    <td align="right">2.54</td>
    <td align="right">2.54</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.78</td>
    <td align="right">3.03</td>
    <td align="right">3.00</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.59</td>
    <td align="right">3.96</td>
    <td align="right">3.96</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.04</td>
    <td align="right">4.64</td>
    <td align="right">4.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.30</td>
    <td align="right">7.69</td>
    <td align="right">5.14</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.62</td>
    <td align="right">8.81</td>
    <td align="right">8.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.57</td>
    <td align="right">8.63</td>
    <td align="right">8.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.38</td>
    <td align="right">10.07</td>
    <td align="right">5.98</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.22</td>
    <td align="right">13.18</td>
    <td align="right">13.18</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.70</td>
    <td align="right">15.35</td>
    <td align="right">15.29</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">24.94</td>
    <td align="right">5.13</td>
    <td align="right">3.50</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.21</td>
    <td align="right">10.46</td>
    <td align="right">13.93</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.70</td>
    <td align="right">3.44</td>
    <td align="right">3.44</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.27</td>
    <td align="right">4.10</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.64</td>
    <td align="right">14.91</td>
    <td align="right">14.68</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.31</td>
    <td align="right">3.86</td>
    <td align="right">3.85</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.93</td>
    <td align="right">4.64</td>
    <td align="right">4.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.19</td>
    <td align="right">18.12</td>
    <td align="right">13.73</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.97</td>
    <td align="right">4.28</td>
    <td align="right">4.26</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">5.57</td>
    <td align="right">5.15</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.79</td>
    <td align="right">23.06</td>
    <td align="right">14.19</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">5.60</td>
    <td align="right">4.64</td>
    <td align="right">4.61</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.16</td>
    <td align="right">5.55</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.21</td>
    <td align="right">11.29</td>
    <td align="right">14.23</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.82</td>
    <td align="right">3.58</td>
    <td align="right">3.58</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.34</td>
    <td align="right">4.14</td>
    <td align="right">4.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.08</td>
    <td align="right">16.18</td>
    <td align="right">15.16</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.38</td>
    <td align="right">3.97</td>
    <td align="right">3.96</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.03</td>
    <td align="right">4.78</td>
    <td align="right">4.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.27</td>
    <td align="right">20.39</td>
    <td align="right">14.01</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.08</td>
    <td align="right">4.38</td>
    <td align="right">4.32</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">5.13</td>
    <td align="right">5.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.80</td>
    <td align="right">25.13</td>
    <td align="right">14.37</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.71</td>
    <td align="right">4.71</td>
    <td align="right">4.69</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.32</td>
    <td align="right">5.57</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.30</td>
    <td align="right">4.31</td>
    <td align="right">4.30</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">8.42</td>
    <td align="right">4.60</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.85</td>
    <td align="right">2.10</td>
    <td align="right">2.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.15</td>
    <td align="right">7.08</td>
    <td align="right">6.98</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.92</td>
    <td align="right">6.80</td>
    <td align="right">6.67</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.77</td>
    <td align="right">2.91</td>
    <td align="right">2.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">11.22</td>
    <td align="right">10.12</td>
    <td align="right">10.08</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">12.36</td>
    <td align="right">10.55</td>
    <td align="right">10.61</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.51</td>
    <td align="right">4.39</td>
    <td align="right">3.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.59</td>
    <td align="right">11.06</td>
    <td align="right">11.00</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.28</td>
    <td align="right">12.44</td>
    <td align="right">12.42</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.30</td>
    <td align="right">4.40</td>
    <td align="right">3.10</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.36</td>
    <td align="right">4.39</td>
    <td align="right">4.38</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.38</td>
    <td align="right">4.69</td>
    <td align="right">4.68</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.85</td>
    <td align="right">2.18</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.22</td>
    <td align="right">7.13</td>
    <td align="right">7.11</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.71</td>
    <td align="right">7.02</td>
    <td align="right">7.00</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.74</td>
    <td align="right">2.97</td>
    <td align="right">2.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.50</td>
    <td align="right">9.80</td>
    <td align="right">9.81</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.32</td>
    <td align="right">10.69</td>
    <td align="right">10.67</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.27</td>
    <td align="right">4.43</td>
    <td align="right">3.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.79</td>
    <td align="right">25.37</td>
    <td align="right">25.38</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.80</td>
    <td align="right">12.48</td>
    <td align="right">12.29</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.34</td>
    <td align="right">4.45</td>
    <td align="right">3.08</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.79</td>
    <td align="right">1.90</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.70</td>
    <td align="right">3.18</td>
    <td align="right">3.18</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.76</td>
    <td align="right">2.99</td>
    <td align="right">2.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.23</td>
    <td align="right">3.27</td>
    <td align="right">2.63</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.21</td>
    <td align="right">3.81</td>
    <td align="right">3.22</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">5.99</td>
    <td align="right">4.50</td>
    <td align="right">3.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.39</td>
    <td align="right">4.21</td>
    <td align="right">2.92</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">7.80</td>
    <td align="right">6.33</td>
    <td align="right">4.83</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">8.54</td>
    <td align="right">6.20</td>
    <td align="right">4.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.42</td>
    <td align="right">4.23</td>
    <td align="right">2.90</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">9.64</td>
    <td align="right">6.81</td>
    <td align="right">4.88</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.75</td>
    <td align="right">6.69</td>
    <td align="right">4.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.81</td>
    <td align="right">2.04</td>
    <td align="right">2.04</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.70</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.76</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.23</td>
    <td align="right">3.43</td>
    <td align="right">2.76</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">3.86</td>
    <td align="right">3.24</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.68</td>
    <td align="right">4.65</td>
    <td align="right">3.96</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.36</td>
    <td align="right">4.31</td>
    <td align="right">3.01</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.91</td>
    <td align="right">6.40</td>
    <td align="right">5.04</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.71</td>
    <td align="right">6.30</td>
    <td align="right">5.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.00</td>
    <td align="right">4.33</td>
    <td align="right">2.99</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.82</td>
    <td align="right">7.05</td>
    <td align="right">5.07</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.05</td>
    <td align="right">14.23</td>
    <td align="right">11.14</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.05</td>
    <td align="right">23.26</td>
    <td align="right">12.60</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">10.06</td>
    <td align="right">10.99</td>
    <td align="right">15.23</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.11</td>
    <td align="right">3.78</td>
    <td align="right">3.64</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.68</td>
    <td align="right">4.51</td>
    <td align="right">4.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.18</td>
    <td align="right">54.03</td>
    <td align="right">23.64</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.61</td>
    <td align="right">6.27</td>
    <td align="right">6.07</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.17</td>
    <td align="right">7.06</td>
    <td align="right">6.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">66.19</td>
    <td align="right">77.52</td>
    <td align="right">25.75</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">15.28</td>
    <td align="right">13.66</td>
    <td align="right">13.78</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">16.47</td>
    <td align="right">16.12</td>
    <td align="right">16.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">97.05</td>
    <td align="right">110.14</td>
    <td align="right">29.84</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">20.91</td>
    <td align="right">17.67</td>
    <td align="right">17.49</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">21.25</td>
    <td align="right">23.51</td>
    <td align="right">23.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.03</td>
    <td align="right">11.77</td>
    <td align="right">15.71</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.25</td>
    <td align="right">3.86</td>
    <td align="right">3.76</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.74</td>
    <td align="right">4.60</td>
    <td align="right">4.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">17.64</td>
    <td align="right">57.49</td>
    <td align="right">24.94</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.48</td>
    <td align="right">5.89</td>
    <td align="right">5.75</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.81</td>
    <td align="right">7.40</td>
    <td align="right">7.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">69.39</td>
    <td align="right">82.35</td>
    <td align="right">26.71</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.56</td>
    <td align="right">13.71</td>
    <td align="right">13.74</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.69</td>
    <td align="right">16.15</td>
    <td align="right">16.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.37</td>
    <td align="right">118.52</td>
    <td align="right">31.49</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.65</td>
    <td align="right">18.35</td>
    <td align="right">18.40</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.93</td>
    <td align="right">22.84</td>
    <td align="right">22.87</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.99</td>
    <td align="right">4.72</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">8.65</td>
    <td align="right">5.03</td>
    <td align="right">4.91</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.20</td>
    <td align="right">2.34</td>
    <td align="right">2.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.58</td>
    <td align="right">9.13</td>
    <td align="right">8.78</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">15.23</td>
    <td align="right">9.57</td>
    <td align="right">8.99</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.94</td>
    <td align="right">4.87</td>
    <td align="right">4.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">26.57</td>
    <td align="right">26.51</td>
    <td align="right">26.85</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">30.37</td>
    <td align="right">29.07</td>
    <td align="right">28.99</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">14.18</td>
    <td align="right">15.42</td>
    <td align="right">11.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">36.17</td>
    <td align="right">35.83</td>
    <td align="right">36.00</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">40.06</td>
    <td align="right">38.40</td>
    <td align="right">38.29</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">16.39</td>
    <td align="right">17.93</td>
    <td align="right">12.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.13</td>
    <td align="right">4.78</td>
    <td align="right">4.67</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.63</td>
    <td align="right">5.17</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.22</td>
    <td align="right">2.46</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.99</td>
    <td align="right">9.92</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.09</td>
    <td align="right">9.68</td>
    <td align="right">9.39</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">5.22</td>
    <td align="right">5.52</td>
    <td align="right">4.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">26.55</td>
    <td align="right">26.95</td>
    <td align="right">27.20</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.65</td>
    <td align="right">29.52</td>
    <td align="right">29.53</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">14.13</td>
    <td align="right">15.58</td>
    <td align="right">11.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.35</td>
    <td align="right">35.74</td>
    <td align="right">35.80</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.59</td>
    <td align="right">38.03</td>
    <td align="right">37.85</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.65</td>
    <td align="right">18.08</td>
    <td align="right">12.52</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.20</td>
    <td align="right">2.16</td>
    <td align="right">2.01</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">4.15</td>
    <td align="right">3.50</td>
    <td align="right">3.37</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">4.24</td>
    <td align="right">3.29</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">5.62</td>
    <td align="right">5.19</td>
    <td align="right">4.06</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">6.15</td>
    <td align="right">10.26</td>
    <td align="right">9.04</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.11</td>
    <td align="right">6.41</td>
    <td align="right">5.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">14.38</td>
    <td align="right">15.19</td>
    <td align="right">10.76</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.93</td>
    <td align="right">18.94</td>
    <td align="right">15.81</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">23.32</td>
    <td align="right">18.63</td>
    <td align="right">15.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">19.37</td>
    <td align="right">19.03</td>
    <td align="right">12.93</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">29.57</td>
    <td align="right">26.86</td>
    <td align="right">19.00</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">29.83</td>
    <td align="right">24.44</td>
    <td align="right">18.73</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.16</td>
    <td align="right">2.31</td>
    <td align="right">2.15</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.09</td>
    <td align="right">3.54</td>
    <td align="right">3.43</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.20</td>
    <td align="right">3.40</td>
    <td align="right">3.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.69</td>
    <td align="right">5.51</td>
    <td align="right">4.34</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.42</td>
    <td align="right">5.64</td>
    <td align="right">4.75</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.75</td>
    <td align="right">6.63</td>
    <td align="right">5.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.38</td>
    <td align="right">15.50</td>
    <td align="right">10.99</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">23.55</td>
    <td align="right">19.36</td>
    <td align="right">16.42</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">21.30</td>
    <td align="right">19.07</td>
    <td align="right">16.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">19.02</td>
    <td align="right">18.79</td>
    <td align="right">12.87</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.69</td>
    <td align="right">26.90</td>
    <td align="right">19.06</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.59</td>
    <td align="right">26.83</td>
    <td align="right">19.02</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.29</td>
    <td align="right">35.05</td>
    <td align="right">14.32</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.75</td>
    <td align="right">43.97</td>
    <td align="right">37.99</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">13.33</td>
    <td align="right">18.27</td>
    <td align="right">18.25</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">17.18</td>
    <td align="right">20.80</td>
    <td align="right">20.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">41.68</td>
    <td align="right">68.08</td>
    <td align="right">41.23</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">18.33</td>
    <td align="right">21.38</td>
    <td align="right">21.38</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.08</td>
    <td align="right">18.83</td>
    <td align="right">18.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">51.16</td>
    <td align="right">84.30</td>
    <td align="right">39.06</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.41</td>
    <td align="right">19.30</td>
    <td align="right">19.11</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">17.37</td>
    <td align="right">21.54</td>
    <td align="right">21.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">64.46</td>
    <td align="right">104.35</td>
    <td align="right">40.54</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.37</td>
    <td align="right">20.60</td>
    <td align="right">20.59</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">19.13</td>
    <td align="right">22.02</td>
    <td align="right">23.09</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.82</td>
    <td align="right">44.11</td>
    <td align="right">37.55</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">16.23</td>
    <td align="right">16.11</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.59</td>
    <td align="right">17.50</td>
    <td align="right">18.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.42</td>
    <td align="right">66.92</td>
    <td align="right">40.45</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.52</td>
    <td align="right">18.23</td>
    <td align="right">18.49</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.10</td>
    <td align="right">19.12</td>
    <td align="right">19.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">57.12</td>
    <td align="right">82.12</td>
    <td align="right">39.39</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.39</td>
    <td align="right">20.49</td>
    <td align="right">20.50</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.01</td>
    <td align="right">21.61</td>
    <td align="right">20.98</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.84</td>
    <td align="right">100.54</td>
    <td align="right">41.20</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">22.17</td>
    <td align="right">22.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.56</td>
    <td align="right">22.63</td>
    <td align="right">22.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.62</td>
    <td align="right">22.05</td>
    <td align="right">22.09</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.60</td>
    <td align="right">25.57</td>
    <td align="right">25.57</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">12.12</td>
    <td align="right">15.55</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.06</td>
    <td align="right">29.63</td>
    <td align="right">29.68</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.22</td>
    <td align="right">32.53</td>
    <td align="right">32.55</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">14.17</td>
    <td align="right">17.82</td>
    <td align="right">17.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.92</td>
    <td align="right">35.38</td>
    <td align="right">35.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.44</td>
    <td align="right">48.11</td>
    <td align="right">48.19</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">16.36</td>
    <td align="right">20.83</td>
    <td align="right">20.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.00</td>
    <td align="right">39.72</td>
    <td align="right">39.74</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.93</td>
    <td align="right">56.28</td>
    <td align="right">56.66</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">23.74</td>
    <td align="right">25.08</td>
    <td align="right">25.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.90</td>
    <td align="right">22.77</td>
    <td align="right">22.74</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.22</td>
    <td align="right">26.53</td>
    <td align="right">26.38</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.27</td>
    <td align="right">15.61</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.46</td>
    <td align="right">30.26</td>
    <td align="right">30.17</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.03</td>
    <td align="right">34.57</td>
    <td align="right">34.58</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.83</td>
    <td align="right">17.77</td>
    <td align="right">18.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.22</td>
    <td align="right">36.81</td>
    <td align="right">36.68</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.66</td>
    <td align="right">48.05</td>
    <td align="right">48.09</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">16.82</td>
    <td align="right">20.85</td>
    <td align="right">20.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.96</td>
    <td align="right">41.84</td>
    <td align="right">41.87</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.52</td>
    <td align="right">56.53</td>
    <td align="right">56.61</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.71</td>
    <td align="right">25.80</td>
    <td align="right">25.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">14.08</td>
    <td align="right">15.72</td>
    <td align="right">15.74</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.59</td>
    <td align="right">22.06</td>
    <td align="right">22.09</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">25.60</td>
    <td align="right">25.56</td>
    <td align="right">25.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">18.88</td>
    <td align="right">19.06</td>
    <td align="right">19.70</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">26.06</td>
    <td align="right">29.62</td>
    <td align="right">29.61</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">36.26</td>
    <td align="right">32.55</td>
    <td align="right">32.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">23.68</td>
    <td align="right">23.54</td>
    <td align="right">23.55</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">31.97</td>
    <td align="right">35.77</td>
    <td align="right">35.41</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">68.44</td>
    <td align="right">48.13</td>
    <td align="right">48.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">30.88</td>
    <td align="right">32.13</td>
    <td align="right">32.01</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.06</td>
    <td align="right">39.75</td>
    <td align="right">39.97</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">82.98</td>
    <td align="right">56.32</td>
    <td align="right">56.66</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.04</td>
    <td align="right">16.89</td>
    <td align="right">16.87</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.95</td>
    <td align="right">22.76</td>
    <td align="right">22.75</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">26.39</td>
    <td align="right">26.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.26</td>
    <td align="right">21.29</td>
    <td align="right">20.42</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.48</td>
    <td align="right">30.25</td>
    <td align="right">30.35</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.03</td>
    <td align="right">34.58</td>
    <td align="right">34.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">22.53</td>
    <td align="right">23.98</td>
    <td align="right">23.98</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.42</td>
    <td align="right">36.81</td>
    <td align="right">36.74</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.84</td>
    <td align="right">48.10</td>
    <td align="right">48.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">30.90</td>
    <td align="right">34.48</td>
    <td align="right">34.47</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.57</td>
    <td align="right">41.85</td>
    <td align="right">41.85</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.61</td>
    <td align="right">56.48</td>
    <td align="right">56.58</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">108.04</td>
    <td align="right">125.92</td>
    <td align="right">27.16</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">36.17</td>
    <td align="right">56.41</td>
    <td align="right">46.69</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">15.66</td>
    <td align="right">21.19</td>
    <td align="right">21.20</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">19.69</td>
    <td align="right">24.27</td>
    <td align="right">24.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">94.02</td>
    <td align="right">134.32</td>
    <td align="right">61.20</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">28.68</td>
    <td align="right">34.89</td>
    <td align="right">35.12</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">26.37</td>
    <td align="right">32.10</td>
    <td align="right">32.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">173.74</td>
    <td align="right">253.14</td>
    <td align="right">79.76</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.28</td>
    <td align="right">46.55</td>
    <td align="right">41.97</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">39.01</td>
    <td align="right">50.21</td>
    <td align="right">50.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">269.01</td>
    <td align="right">405.03</td>
    <td align="right">98.03</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.63</td>
    <td align="right">62.37</td>
    <td align="right">62.31</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">61.49</td>
    <td align="right">65.33</td>
    <td align="right">66.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">38.40</td>
    <td align="right">54.64</td>
    <td align="right">45.64</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.01</td>
    <td align="right">19.53</td>
    <td align="right">19.56</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.47</td>
    <td align="right">20.63</td>
    <td align="right">20.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">100.66</td>
    <td align="right">130.00</td>
    <td align="right">60.63</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.49</td>
    <td align="right">28.71</td>
    <td align="right">28.68</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.25</td>
    <td align="right">32.41</td>
    <td align="right">32.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">190.86</td>
    <td align="right">251.21</td>
    <td align="right">79.23</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.69</td>
    <td align="right">47.93</td>
    <td align="right">47.98</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">39.03</td>
    <td align="right">50.18</td>
    <td align="right">50.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">297.69</td>
    <td align="right">405.03</td>
    <td align="right">98.93</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.42</td>
    <td align="right">64.16</td>
    <td align="right">64.16</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.20</td>
    <td align="right">65.20</td>
    <td align="right">65.07</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.67</td>
    <td align="right">26.31</td>
    <td align="right">26.41</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.14</td>
    <td align="right">31.40</td>
    <td align="right">31.36</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">14.67</td>
    <td align="right">18.21</td>
    <td align="right">18.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">40.03</td>
    <td align="right">44.77</td>
    <td align="right">44.65</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">53.82</td>
    <td align="right">52.03</td>
    <td align="right">50.38</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">24.05</td>
    <td align="right">27.79</td>
    <td align="right">27.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">66.57</td>
    <td align="right">71.17</td>
    <td align="right">71.21</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">103.01</td>
    <td align="right">83.12</td>
    <td align="right">83.09</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">41.42</td>
    <td align="right">45.35</td>
    <td align="right">45.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.11</td>
    <td align="right">91.40</td>
    <td align="right">91.54</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">135.23</td>
    <td align="right">107.72</td>
    <td align="right">107.89</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">70.10</td>
    <td align="right">75.83</td>
    <td align="right">75.82</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.38</td>
    <td align="right">26.38</td>
    <td align="right">26.33</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.48</td>
    <td align="right">31.83</td>
    <td align="right">31.78</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.93</td>
    <td align="right">18.97</td>
    <td align="right">18.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">41.18</td>
    <td align="right">44.12</td>
    <td align="right">44.20</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.64</td>
    <td align="right">51.97</td>
    <td align="right">51.93</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">24.46</td>
    <td align="right">27.79</td>
    <td align="right">27.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.64</td>
    <td align="right">73.01</td>
    <td align="right">73.05</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.80</td>
    <td align="right">82.26</td>
    <td align="right">82.34</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">41.42</td>
    <td align="right">44.87</td>
    <td align="right">44.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.39</td>
    <td align="right">94.91</td>
    <td align="right">94.86</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.12</td>
    <td align="right">108.76</td>
    <td align="right">108.82</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.27</td>
    <td align="right">76.78</td>
    <td align="right">76.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">15.94</td>
    <td align="right">18.14</td>
    <td align="right">17.81</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">24.14</td>
    <td align="right">26.69</td>
    <td align="right">26.75</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">30.23</td>
    <td align="right">32.73</td>
    <td align="right">31.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">30.19</td>
    <td align="right">30.78</td>
    <td align="right">30.77</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">39.21</td>
    <td align="right">43.74</td>
    <td align="right">43.75</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">52.60</td>
    <td align="right">51.03</td>
    <td align="right">49.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">47.74</td>
    <td align="right">47.98</td>
    <td align="right">47.85</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">66.05</td>
    <td align="right">70.72</td>
    <td align="right">70.84</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">101.86</td>
    <td align="right">81.39</td>
    <td align="right">81.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">81.25</td>
    <td align="right">85.01</td>
    <td align="right">84.32</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">87.93</td>
    <td align="right">92.62</td>
    <td align="right">92.69</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">134.52</td>
    <td align="right">113.16</td>
    <td align="right">110.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">16.03</td>
    <td align="right">19.74</td>
    <td align="right">19.82</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">24.50</td>
    <td align="right">27.29</td>
    <td align="right">27.40</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.72</td>
    <td align="right">32.19</td>
    <td align="right">32.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.58</td>
    <td align="right">32.24</td>
    <td align="right">32.01</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.28</td>
    <td align="right">44.77</td>
    <td align="right">44.65</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.04</td>
    <td align="right">52.05</td>
    <td align="right">52.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">47.45</td>
    <td align="right">48.76</td>
    <td align="right">48.73</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.28</td>
    <td align="right">72.81</td>
    <td align="right">72.80</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">103.35</td>
    <td align="right">83.04</td>
    <td align="right">83.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.53</td>
    <td align="right">86.97</td>
    <td align="right">87.04</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.50</td>
    <td align="right">95.00</td>
    <td align="right">95.01</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">135.45</td>
    <td align="right">109.10</td>
    <td align="right">110.19</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">79.26</td>
    <td align="right">14.03</td>
    <td align="right">8.58</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">15.82</td>
    <td align="right">23.22</td>
    <td align="right">26.72</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.09</td>
    <td align="right">13.44</td>
    <td align="right">13.46</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">14.85</td>
    <td align="right">16.24</td>
    <td align="right">16.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">22.37</td>
    <td align="right">34.54</td>
    <td align="right">29.07</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">15.37</td>
    <td align="right">16.76</td>
    <td align="right">16.76</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">17.15</td>
    <td align="right">18.84</td>
    <td align="right">18.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">27.94</td>
    <td align="right">42.25</td>
    <td align="right">29.10</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.72</td>
    <td align="right">19.12</td>
    <td align="right">19.18</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">20.71</td>
    <td align="right">22.04</td>
    <td align="right">22.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">35.65</td>
    <td align="right">61.82</td>
    <td align="right">30.03</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">21.07</td>
    <td align="right">22.44</td>
    <td align="right">22.25</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">23.28</td>
    <td align="right">24.36</td>
    <td align="right">24.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.42</td>
    <td align="right">28.18</td>
    <td align="right">29.27</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.46</td>
    <td align="right">13.95</td>
    <td align="right">14.05</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.86</td>
    <td align="right">18.05</td>
    <td align="right">18.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.72</td>
    <td align="right">42.78</td>
    <td align="right">31.48</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.03</td>
    <td align="right">18.43</td>
    <td align="right">18.51</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.19</td>
    <td align="right">20.72</td>
    <td align="right">20.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.54</td>
    <td align="right">64.20</td>
    <td align="right">32.31</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.59</td>
    <td align="right">21.20</td>
    <td align="right">21.33</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.04</td>
    <td align="right">22.91</td>
    <td align="right">22.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">58.83</td>
    <td align="right">81.24</td>
    <td align="right">32.90</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.18</td>
    <td align="right">23.17</td>
    <td align="right">23.25</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.06</td>
    <td align="right">25.72</td>
    <td align="right">25.72</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.29</td>
    <td align="right">17.05</td>
    <td align="right">17.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.01</td>
    <td align="right">17.19</td>
    <td align="right">17.21</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.81</td>
    <td align="right">8.68</td>
    <td align="right">8.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.94</td>
    <td align="right">25.87</td>
    <td align="right">26.04</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.24</td>
    <td align="right">26.07</td>
    <td align="right">26.08</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.07</td>
    <td align="right">12.42</td>
    <td align="right">12.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.31</td>
    <td align="right">36.42</td>
    <td align="right">36.40</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.43</td>
    <td align="right">35.94</td>
    <td align="right">35.86</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.58</td>
    <td align="right">15.41</td>
    <td align="right">15.42</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.42</td>
    <td align="right">38.83</td>
    <td align="right">38.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.63</td>
    <td align="right">40.53</td>
    <td align="right">40.70</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">17.63</td>
    <td align="right">20.28</td>
    <td align="right">20.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.04</td>
    <td align="right">18.48</td>
    <td align="right">18.35</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.09</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">8.00</td>
    <td align="right">8.72</td>
    <td align="right">8.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.72</td>
    <td align="right">26.57</td>
    <td align="right">26.61</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.58</td>
    <td align="right">26.94</td>
    <td align="right">26.93</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.93</td>
    <td align="right">13.76</td>
    <td align="right">13.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.20</td>
    <td align="right">35.36</td>
    <td align="right">35.32</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.60</td>
    <td align="right">34.50</td>
    <td align="right">34.53</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.83</td>
    <td align="right">17.82</td>
    <td align="right">17.83</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.59</td>
    <td align="right">38.28</td>
    <td align="right">38.27</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.36</td>
    <td align="right">41.03</td>
    <td align="right">41.13</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">19.74</td>
    <td align="right">19.74</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">7.45</td>
    <td align="right">8.49</td>
    <td align="right">8.49</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">17.27</td>
    <td align="right">17.02</td>
    <td align="right">17.02</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">16.15</td>
    <td align="right">17.19</td>
    <td align="right">17.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">10.97</td>
    <td align="right">12.18</td>
    <td align="right">12.18</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.93</td>
    <td align="right">25.85</td>
    <td align="right">26.02</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">24.26</td>
    <td align="right">26.08</td>
    <td align="right">26.09</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">13.00</td>
    <td align="right">15.30</td>
    <td align="right">15.21</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">34.29</td>
    <td align="right">36.39</td>
    <td align="right">36.45</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">33.33</td>
    <td align="right">35.75</td>
    <td align="right">35.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">17.53</td>
    <td align="right">19.06</td>
    <td align="right">19.06</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">37.46</td>
    <td align="right">38.83</td>
    <td align="right">38.83</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">42.57</td>
    <td align="right">40.59</td>
    <td align="right">40.65</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.62</td>
    <td align="right">9.01</td>
    <td align="right">8.47</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.06</td>
    <td align="right">18.44</td>
    <td align="right">18.35</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.03</td>
    <td align="right">18.84</td>
    <td align="right">18.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.85</td>
    <td align="right">14.08</td>
    <td align="right">14.08</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.57</td>
    <td align="right">26.59</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">26.98</td>
    <td align="right">26.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.30</td>
    <td align="right">17.23</td>
    <td align="right">17.23</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">35.34</td>
    <td align="right">35.34</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.54</td>
    <td align="right">34.46</td>
    <td align="right">34.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.83</td>
    <td align="right">20.00</td>
    <td align="right">20.01</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.51</td>
    <td align="right">38.30</td>
    <td align="right">38.30</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.44</td>
    <td align="right">41.10</td>
    <td align="right">41.09</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.07</td>
    <td align="right">62.74</td>
    <td align="right">24.01</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">20.63</td>
    <td align="right">29.81</td>
    <td align="right">31.69</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.45</td>
    <td align="right">15.88</td>
    <td align="right">15.96</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.62</td>
    <td align="right">18.85</td>
    <td align="right">18.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">57.13</td>
    <td align="right">76.06</td>
    <td align="right">41.73</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">26.01</td>
    <td align="right">27.03</td>
    <td align="right">27.28</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">28.26</td>
    <td align="right">32.23</td>
    <td align="right">32.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">112.61</td>
    <td align="right">156.28</td>
    <td align="right">57.40</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">38.54</td>
    <td align="right">45.41</td>
    <td align="right">45.31</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">49.92</td>
    <td align="right">50.55</td>
    <td align="right">50.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">165.11</td>
    <td align="right">239.04</td>
    <td align="right">71.94</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">63.14</td>
    <td align="right">63.98</td>
    <td align="right">63.82</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">67.11</td>
    <td align="right">67.83</td>
    <td align="right">67.67</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">34.58</td>
    <td align="right">42.98</td>
    <td align="right">37.06</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.62</td>
    <td align="right">18.19</td>
    <td align="right">18.04</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.27</td>
    <td align="right">20.21</td>
    <td align="right">20.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">75.63</td>
    <td align="right">92.68</td>
    <td align="right">46.17</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.61</td>
    <td align="right">27.48</td>
    <td align="right">27.28</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.84</td>
    <td align="right">33.98</td>
    <td align="right">34.27</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">140.69</td>
    <td align="right">200.84</td>
    <td align="right">66.45</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.40</td>
    <td align="right">46.93</td>
    <td align="right">46.94</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">50.52</td>
    <td align="right">49.95</td>
    <td align="right">49.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.06</td>
    <td align="right">326.14</td>
    <td align="right">82.91</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.18</td>
    <td align="right">63.81</td>
    <td align="right">64.03</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.24</td>
    <td align="right">68.84</td>
    <td align="right">68.88</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">18.87</td>
    <td align="right">19.01</td>
    <td align="right">19.16</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">18.34</td>
    <td align="right">20.10</td>
    <td align="right">20.13</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">9.05</td>
    <td align="right">10.55</td>
    <td align="right">10.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">34.39</td>
    <td align="right">39.91</td>
    <td align="right">40.24</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">36.66</td>
    <td align="right">39.86</td>
    <td align="right">39.92</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">19.29</td>
    <td align="right">19.72</td>
    <td align="right">19.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">68.00</td>
    <td align="right">69.84</td>
    <td align="right">72.20</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.12</td>
    <td align="right">70.76</td>
    <td align="right">70.76</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">36.70</td>
    <td align="right">38.78</td>
    <td align="right">38.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">86.81</td>
    <td align="right">85.16</td>
    <td align="right">85.21</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.73</td>
    <td align="right">93.16</td>
    <td align="right">94.56</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">51.66</td>
    <td align="right">51.79</td>
    <td align="right">51.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.15</td>
    <td align="right">21.73</td>
    <td align="right">21.62</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.69</td>
    <td align="right">22.29</td>
    <td align="right">22.55</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">10.07</td>
    <td align="right">11.89</td>
    <td align="right">11.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.01</td>
    <td align="right">39.67</td>
    <td align="right">39.83</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">43.38</td>
    <td align="right">44.92</td>
    <td align="right">44.79</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">22.87</td>
    <td align="right">25.06</td>
    <td align="right">25.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">68.84</td>
    <td align="right">70.44</td>
    <td align="right">70.40</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.92</td>
    <td align="right">68.66</td>
    <td align="right">69.75</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">38.34</td>
    <td align="right">41.07</td>
    <td align="right">41.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.65</td>
    <td align="right">88.54</td>
    <td align="right">89.53</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.00</td>
    <td align="right">92.68</td>
    <td align="right">93.65</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">52.83</td>
    <td align="right">51.44</td>
    <td align="right">54.12</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">8.35</td>
    <td align="right">9.22</td>
    <td align="right">9.53</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">19.46</td>
    <td align="right">19.47</td>
    <td align="right">19.67</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">18.96</td>
    <td align="right">20.25</td>
    <td align="right">20.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">20.54</td>
    <td align="right">22.80</td>
    <td align="right">23.42</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">33.31</td>
    <td align="right">38.56</td>
    <td align="right">38.85</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">38.51</td>
    <td align="right">37.30</td>
    <td align="right">37.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">36.46</td>
    <td align="right">40.40</td>
    <td align="right">39.57</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">67.76</td>
    <td align="right">68.53</td>
    <td align="right">68.51</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">67.37</td>
    <td align="right">68.78</td>
    <td align="right">69.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">51.10</td>
    <td align="right">50.65</td>
    <td align="right">50.69</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">88.13</td>
    <td align="right">88.90</td>
    <td align="right">88.91</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">94.22</td>
    <td align="right">90.66</td>
    <td align="right">92.22</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">9.26</td>
    <td align="right">11.13</td>
    <td align="right">10.44</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.96</td>
    <td align="right">21.50</td>
    <td align="right">21.48</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.48</td>
    <td align="right">22.14</td>
    <td align="right">22.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.17</td>
    <td align="right">24.21</td>
    <td align="right">24.20</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">37.03</td>
    <td align="right">42.45</td>
    <td align="right">42.45</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.65</td>
    <td align="right">44.75</td>
    <td align="right">44.77</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.95</td>
    <td align="right">40.79</td>
    <td align="right">40.69</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.51</td>
    <td align="right">69.17</td>
    <td align="right">69.44</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.77</td>
    <td align="right">68.44</td>
    <td align="right">68.60</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.20</td>
    <td align="right">53.02</td>
    <td align="right">53.02</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.09</td>
    <td align="right">88.89</td>
    <td align="right">88.99</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">97.14</td>
    <td align="right">93.74</td>
    <td align="right">94.97</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">31.69</td>
    <td align="right">6.64</td>
    <td align="right">5.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">51.89</td>
    <td align="right">43.65</td>
    <td align="right">32.63</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.21</td>
    <td align="right">18.47</td>
    <td align="right">21.61</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">23.19</td>
    <td align="right">23.93</td>
    <td align="right">23.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">77.55</td>
    <td align="right">65.12</td>
    <td align="right">33.59</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">19.50</td>
    <td align="right">19.70</td>
    <td align="right">21.62</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.05</td>
    <td align="right">25.32</td>
    <td align="right">26.68</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">95.00</td>
    <td align="right">79.33</td>
    <td align="right">32.95</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">23.13</td>
    <td align="right">23.01</td>
    <td align="right">24.24</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.37</td>
    <td align="right">27.38</td>
    <td align="right">28.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">119.92</td>
    <td align="right">101.35</td>
    <td align="right">34.49</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">24.24</td>
    <td align="right">24.43</td>
    <td align="right">25.29</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">29.28</td>
    <td align="right">28.24</td>
    <td align="right">29.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.48</td>
    <td align="right">59.39</td>
    <td align="right">39.82</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.85</td>
    <td align="right">20.59</td>
    <td align="right">23.04</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.59</td>
    <td align="right">25.05</td>
    <td align="right">26.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">99.45</td>
    <td align="right">85.84</td>
    <td align="right">42.11</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.17</td>
    <td align="right">22.01</td>
    <td align="right">23.19</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.42</td>
    <td align="right">27.72</td>
    <td align="right">28.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">123.02</td>
    <td align="right">103.89</td>
    <td align="right">41.11</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.14</td>
    <td align="right">25.32</td>
    <td align="right">25.80</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">28.90</td>
    <td align="right">29.82</td>
    <td align="right">29.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">160.80</td>
    <td align="right">132.66</td>
    <td align="right">41.54</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">26.78</td>
    <td align="right">26.49</td>
    <td align="right">27.10</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.11</td>
    <td align="right">31.99</td>
    <td align="right">32.03</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">21.14</td>
    <td align="right">39.24</td>
    <td align="right">40.28</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">23.57</td>
    <td align="right">38.99</td>
    <td align="right">39.21</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">16.02</td>
    <td align="right">27.66</td>
    <td align="right">27.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">25.85</td>
    <td align="right">54.42</td>
    <td align="right">54.46</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">30.00</td>
    <td align="right">55.43</td>
    <td align="right">54.88</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.54</td>
    <td align="right">37.21</td>
    <td align="right">26.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.63</td>
    <td align="right">73.27</td>
    <td align="right">72.23</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">40.83</td>
    <td align="right">74.73</td>
    <td align="right">71.84</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">25.61</td>
    <td align="right">54.27</td>
    <td align="right">36.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">39.70</td>
    <td align="right">82.09</td>
    <td align="right">82.17</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">46.25</td>
    <td align="right">86.79</td>
    <td align="right">86.08</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">25.60</td>
    <td align="right">54.60</td>
    <td align="right">37.44</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.45</td>
    <td align="right">41.12</td>
    <td align="right">41.84</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.26</td>
    <td align="right">42.14</td>
    <td align="right">42.82</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.52</td>
    <td align="right">28.48</td>
    <td align="right">28.43</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.42</td>
    <td align="right">56.97</td>
    <td align="right">56.80</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">31.79</td>
    <td align="right">57.40</td>
    <td align="right">57.00</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.74</td>
    <td align="right">37.41</td>
    <td align="right">27.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">38.03</td>
    <td align="right">76.26</td>
    <td align="right">74.76</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.14</td>
    <td align="right">75.04</td>
    <td align="right">74.72</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.07</td>
    <td align="right">53.94</td>
    <td align="right">37.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.11</td>
    <td align="right">84.75</td>
    <td align="right">85.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">46.63</td>
    <td align="right">89.78</td>
    <td align="right">89.76</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.15</td>
    <td align="right">54.31</td>
    <td align="right">37.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">16.52</td>
    <td align="right">27.45</td>
    <td align="right">27.41</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">18.51</td>
    <td align="right">30.05</td>
    <td align="right">30.01</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">19.21</td>
    <td align="right">29.83</td>
    <td align="right">29.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">16.56</td>
    <td align="right">44.18</td>
    <td align="right">34.83</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">17.43</td>
    <td align="right">38.47</td>
    <td align="right">28.95</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">19.03</td>
    <td align="right">47.27</td>
    <td align="right">37.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">26.10</td>
    <td align="right">53.33</td>
    <td align="right">36.31</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">30.04</td>
    <td align="right">57.85</td>
    <td align="right">39.50</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">30.88</td>
    <td align="right">57.80</td>
    <td align="right">39.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">26.47</td>
    <td align="right">54.14</td>
    <td align="right">36.81</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">31.13</td>
    <td align="right">59.56</td>
    <td align="right">40.27</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">32.04</td>
    <td align="right">59.02</td>
    <td align="right">39.79</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.95</td>
    <td align="right">28.23</td>
    <td align="right">28.21</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.71</td>
    <td align="right">30.68</td>
    <td align="right">30.63</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.31</td>
    <td align="right">30.73</td>
    <td align="right">30.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">17.93</td>
    <td align="right">44.36</td>
    <td align="right">34.87</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.81</td>
    <td align="right">38.63</td>
    <td align="right">29.08</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.68</td>
    <td align="right">46.81</td>
    <td align="right">37.54</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.08</td>
    <td align="right">53.56</td>
    <td align="right">36.71</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.90</td>
    <td align="right">57.72</td>
    <td align="right">40.14</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.73</td>
    <td align="right">57.41</td>
    <td align="right">39.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.22</td>
    <td align="right">53.90</td>
    <td align="right">36.78</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">32.69</td>
    <td align="right">59.49</td>
    <td align="right">40.51</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">33.95</td>
    <td align="right">58.79</td>
    <td align="right">39.74</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.95</td>
    <td align="right">33.55</td>
    <td align="right">20.67</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">54.06</td>
    <td align="right">47.71</td>
    <td align="right">35.51</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">18.39</td>
    <td align="right">18.61</td>
    <td align="right">22.05</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.67</td>
    <td align="right">25.32</td>
    <td align="right">26.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">137.10</td>
    <td align="right">144.72</td>
    <td align="right">57.72</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">21.49</td>
    <td align="right">21.31</td>
    <td align="right">23.18</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">28.26</td>
    <td align="right">31.92</td>
    <td align="right">33.42</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">207.20</td>
    <td align="right">181.50</td>
    <td align="right">57.02</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">35.21</td>
    <td align="right">35.14</td>
    <td align="right">36.51</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">46.19</td>
    <td align="right">45.83</td>
    <td align="right">47.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">345.50</td>
    <td align="right">292.40</td>
    <td align="right">72.15</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">42.55</td>
    <td align="right">42.53</td>
    <td align="right">43.79</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">58.87</td>
    <td align="right">59.71</td>
    <td align="right">60.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">69.93</td>
    <td align="right">62.22</td>
    <td align="right">42.49</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.03</td>
    <td align="right">20.78</td>
    <td align="right">23.36</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.89</td>
    <td align="right">27.07</td>
    <td align="right">28.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">124.28</td>
    <td align="right">116.31</td>
    <td align="right">50.44</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.23</td>
    <td align="right">23.51</td>
    <td align="right">24.48</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">31.33</td>
    <td align="right">34.78</td>
    <td align="right">35.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">258.27</td>
    <td align="right">215.55</td>
    <td align="right">64.03</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.30</td>
    <td align="right">37.07</td>
    <td align="right">38.03</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.36</td>
    <td align="right">48.22</td>
    <td align="right">47.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">433.56</td>
    <td align="right">353.43</td>
    <td align="right">78.74</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.10</td>
    <td align="right">44.73</td>
    <td align="right">45.39</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.44</td>
    <td align="right">62.14</td>
    <td align="right">62.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">23.07</td>
    <td align="right">39.53</td>
    <td align="right">40.45</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.84</td>
    <td align="right">39.16</td>
    <td align="right">39.46</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">16.28</td>
    <td align="right">29.53</td>
    <td align="right">29.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.67</td>
    <td align="right">56.02</td>
    <td align="right">56.08</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.31</td>
    <td align="right">62.35</td>
    <td align="right">62.68</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">17.46</td>
    <td align="right">40.20</td>
    <td align="right">29.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">55.29</td>
    <td align="right">85.33</td>
    <td align="right">85.37</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">63.02</td>
    <td align="right">91.25</td>
    <td align="right">88.72</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">45.88</td>
    <td align="right">78.87</td>
    <td align="right">62.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">73.41</td>
    <td align="right">104.53</td>
    <td align="right">104.72</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">84.12</td>
    <td align="right">115.81</td>
    <td align="right">115.01</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">57.60</td>
    <td align="right">91.99</td>
    <td align="right">74.98</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">25.94</td>
    <td align="right">41.35</td>
    <td align="right">42.01</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.73</td>
    <td align="right">47.88</td>
    <td align="right">48.84</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.00</td>
    <td align="right">30.32</td>
    <td align="right">30.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.35</td>
    <td align="right">58.41</td>
    <td align="right">57.86</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">36.96</td>
    <td align="right">59.26</td>
    <td align="right">58.44</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">18.89</td>
    <td align="right">40.09</td>
    <td align="right">30.21</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.60</td>
    <td align="right">88.42</td>
    <td align="right">86.94</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.23</td>
    <td align="right">90.89</td>
    <td align="right">90.60</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">46.97</td>
    <td align="right">76.64</td>
    <td align="right">60.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.88</td>
    <td align="right">106.46</td>
    <td align="right">107.63</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.45</td>
    <td align="right">117.79</td>
    <td align="right">117.67</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">58.67</td>
    <td align="right">89.64</td>
    <td align="right">74.34</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">17.32</td>
    <td align="right">29.06</td>
    <td align="right">29.03</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">18.74</td>
    <td align="right">31.39</td>
    <td align="right">31.38</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">19.42</td>
    <td align="right">30.93</td>
    <td align="right">30.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">18.82</td>
    <td align="right">47.52</td>
    <td align="right">38.42</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.02</td>
    <td align="right">40.57</td>
    <td align="right">30.69</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.18</td>
    <td align="right">50.26</td>
    <td align="right">40.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">47.37</td>
    <td align="right">76.68</td>
    <td align="right">60.85</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">50.66</td>
    <td align="right">81.91</td>
    <td align="right">63.49</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">52.22</td>
    <td align="right">82.43</td>
    <td align="right">65.16</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">58.98</td>
    <td align="right">90.73</td>
    <td align="right">74.93</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">61.47</td>
    <td align="right">96.85</td>
    <td align="right">77.98</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">62.94</td>
    <td align="right">97.54</td>
    <td align="right">78.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>>*</code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1>*</code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.18</td>
    <td align="right">29.90</td>
    <td align="right">29.87</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.03</td>
    <td align="right">32.01</td>
    <td align="right">31.97</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.53</td>
    <td align="right">31.86</td>
    <td align="right">31.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">19.78</td>
    <td align="right">53.88</td>
    <td align="right">44.59</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.49</td>
    <td align="right">44.60</td>
    <td align="right">35.01</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">23.57</td>
    <td align="right">50.66</td>
    <td align="right">41.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">49.68</td>
    <td align="right">77.03</td>
    <td align="right">60.19</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">52.39</td>
    <td align="right">81.42</td>
    <td align="right">63.67</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.55</td>
    <td align="right">81.53</td>
    <td align="right">63.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.79</td>
    <td align="right">91.98</td>
    <td align="right">75.16</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">68.56</td>
    <td align="right">102.11</td>
    <td align="right">82.38</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">64.74</td>
    <td align="right">98.01</td>
    <td align="right">78.35</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
